# Referências e Comandos Testados

## Referências

- [YouTube - Como usar Ollama](https://www.youtube.com/watch?v=80w4GVlp_qY)
- [YouTube - Introdução ao pgvector](https://www.youtube.com/watch?v=8KFE_4fvXG4)

- [Ollama - Pesquisa](https://ollama.com/search)
- [Docker Hub - Ollama](https://hub.docker.com/r/ollama/ollama)

- [GitHub - pgvector](https://github.com/pgvector/pgvector)
- [Docker Hub - pgvector](https://hub.docker.com/r/pgvector/pgvector)

- [GitHub - Timescale/pgai](https://github.com/timescale/pgai)
- [GitHub - Ollama](https://github.com/ollama/ollama)

## Comandos Testados

### Inicialização com Docker Compose
```bash
docker compose up -d
```

### PgVector
```bash
docker pull pgvector/pgvector:pg17
```

### Timescale/pgAI
```bash
docker run -d --name pgai -p 5432:5432 -v pg-data:/home/postgres/pgdata/data -e POSTGRES_PASSWORD=password timescale/timescaledb-ha:pg17
docker exec -it pgai psql -U postgres -c "CREATE EXTENSION IF NOT EXISTS ai CASCADE;"
```

### Ollama
```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama run mistral
```

---

**Autor:** Gustavo das Neves Ubeda 
**Contato:** [gustavo.n.ubeda@gmail.com.br](mailto:gustavo.n.ubeda@gmail.com.br)
**Linkdin:** [LinkedIn](https://www.linkedin.com/in/gustavoubeda/)
