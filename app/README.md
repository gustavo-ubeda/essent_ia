https://fastapi.tiangolo.com/deployment/docker/
docker build -t busec .
docker run -d --name busec_api -p 80:80 busec

docker network create busec_network
docker network connect busec_network busec_api
docker network connect busec_network pgvector

docker exec -it busec_api ping pgvector

http://localhost/docs
http://localhost/redoc