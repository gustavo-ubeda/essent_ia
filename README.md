# CASE: Busca Semântica + PGvector

**Autor:** Gustavo das Neves Ubeda

**Contato:** [gustavo.n.ubeda@gmail.com.br](mailto:gustavo.n.ubeda@gmail.com.br)

**Linkdin:** [LinkedIn](https://www.linkedin.com/in/gustavoubeda/)

### Instalação do Docker

Para instalar e rodar o Docker, consulte a documentação: [Docker Desktop](https://www.docker.com/products/docker-desktop/).

---

### Instalação do Postgre com PGvector

Para instalar e rodar o PostgreSQL com a extensão PGvector, siga os passos abaixo:

1. Consulte a documentação: [PGvector no GitHub](https://github.com/pgvector/pgvector#getting-started).
2. Baixe a imagem Docker:
   ```bash
   docker pull pgvector/pgvector:pg17
   ```
3. Execute o container com a imagem:
   ```bash
   docker run -d --name pgvector -p 5432:5432 -v pg-data:/home/postgres/pgdata/data -e POSTGRES_PASSWORD=password pgvector/pgvector:pg17
   ```

---

### Instalação do Ollama

Para instalar e rodar o Ollama, siga os passos abaixo:

1. Consulte a documentação: [Ollama no GitHub](https://github.com/ollama/ollama/blob/main/docs/api.md).
2. Baixe e execute a imagem Docker:
   ```bash
   docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
   ```
3. Execute os modelos de IA disponíveis:
   - **Mistral:**
     ```bash
     docker exec -it ollama ollama run mistral
     ```
   - **Llama3:**
     ```bash
     docker exec -it ollama ollama run llama3
     ```
   - **Nomic Embed Text:**
     ```bash
     docker exec -it ollama ollama run nomic-embed-text
     ```

### Referências

- [YouTube - Como usar Ollama](https://www.youtube.com/watch?v=80w4GVlp_qY)
- [YouTube - Introdução ao pgvector](https://www.youtube.com/watch?v=8KFE_4fvXG4)

- [Ollama - Pesquisa](https://ollama.com/search)
- [Docker Hub - Ollama](https://hub.docker.com/r/ollama/ollama)

- [GitHub - pgvector](https://github.com/pgvector/pgvector)
- [Docker Hub - pgvector](https://hub.docker.com/r/pgvector/pgvector)

- [GitHub - Timescale/pgai](https://github.com/timescale/pgai)
- [GitHub - Ollama](https://github.com/ollama/ollama)
