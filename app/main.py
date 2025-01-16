# https://fastapi.tiangolo.com/deployment/docker
from fastapi import FastAPI
from pydantic import BaseModel

from busec_funcs import upsert_data, busca_semantica, create_embed

app = FastAPI()


@app.get("/busca-semantica/{text}")
def busec(text):
    return busca_semantica(text).drop(columns=["embedding"]).to_dict(orient="records")

@app.get("/create-emb/{text}")
def cemb(text):
    return create_embed(text)

class Item(BaseModel):
    id_produto: int
    nome_produto: str
    laboratorio: str
    substancia: str
    apresentacao: str
    classe_terapeutica: str
    tipo_produto: str
    tarja: str


@app.post("/upsert/")
def create_item(item: Item):
    data = item.dict()
    return upsert_data(data).to_dict(orient="records")