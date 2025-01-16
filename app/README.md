# Guia de Implantação com Docker

## Referências

- [Documentação Oficial do FastAPI sobre Docker](https://fastapi.tiangolo.com/deployment/docker/)

## Comandos para Implantação

### Build da Imagem Docker
```bash
docker build -t busec .
```

### Execução do Contêiner FastAPI
```bash
docker run -d --name busec_api -p 80:80 busec
```

### Configuração de Redes Docker
#### Criação da Rede
```bash
docker network create busec_network
```

#### Conexão dos Contêineres à Rede
```bash
docker network connect busec_network busec_api
docker network connect busec_network pgvector
```

### Teste de Comunicação entre os Contêineres
```bash
docker exec -it busec_api ping pgvector
```

## Endpoints Disponíveis
- [Documentação Interativa (Swagger UI)](http://localhost/docs)
- [Documentação Alternativa (ReDoc)](http://localhost/redoc)

---

**Autor:** Gustavo Ubeda  
**Contato:** [LinkedIn](https://www.linkedin.com/in/gustavoubeda/)
