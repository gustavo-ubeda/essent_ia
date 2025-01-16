import requests
import psycopg2
import pandas as pd

# Ollama API
ollama_host = "http://host.docker.internal:11434"
model_use = "nomic-embed-text" # mistral, llama3, nomic-embed-text

# Postgres +  PGvector
dbname ='postgres'
user = 'postgres'
password = 'password'
host = 'host.docker.internal'
port = '5432'

# Abstração para excução de querys no Postgres
def exe_query(query):
    conn = psycopg2.connect(dbname=dbname,user=user,password=password,host=host,port=port)
    cur = conn.cursor()
    cur.execute(query)

    try:
        data = cur.fetchall()
        cols = [desc[0] for desc in cur.description]

        conn.commit()
        cur.close()
        conn.close()

        return pd.DataFrame(data, columns=cols)
    except:
        conn.commit()
        cur.close()
        conn.close()

        return []
    
# Gera o embedding para o texto a partir do modelo selecionado
def create_embed(text, model=model_use):
    data = {
        "model": model,
        "input": text
    }
    response = requests.post(f"{ollama_host}/api/embed", json=data)

    try:
        return response.json()["embeddings"][0]
    except:
        print(response.json())

def upsert_data(data):
    text_to_embed = f"{data['nome_produto']} ({data['apresentacao']}) - {data['tarja']} - Contém: {data['substancia']}"
    embed = create_embed(text_to_embed, model=model_use)
    data["embedding"] = str(embed)
    
    cols = ", ".join([i for i in data])
    vals = tuple([data[i] for i in data])

    qr = f"""
    INSERT INTO produtos ({cols}) VALUES {vals}
    ON CONFLICT (id_produto)
    DO UPDATE SET
        nome_produto = EXCLUDED.nome_produto,
        laboratorio = EXCLUDED.laboratorio,
        substancia = EXCLUDED.substancia,
        apresentacao = EXCLUDED.apresentacao,
        classe_terapeutica = EXCLUDED.classe_terapeutica,
        tipo_produto = EXCLUDED.tipo_produto,
        tarja = EXCLUDED.tarja,
        embedding = EXCLUDED.embedding;
    """

    exe_query(qr)
    return exe_query(f"SELECT * FROM produtos WHERE id_produto = {data['id_produto']}")

# Busca semântica por coseno sentre vetores
# Obs: Produto interno (<#>), distância cosseno (<=>), distância L2 (<->) e distância L1 (<+>
def busca_semantica(tx, n_itens=5):
    embed = create_embed(tx, model=model_use)

    qr = f"SELECT * FROM produtos ORDER BY embedding <=> '{embed}' LIMIT {n_itens};"
    return exe_query(qr)