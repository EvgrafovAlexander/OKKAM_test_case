# OKKAM_test_case

docker-compose --force-recreate --file docker-compose.yml up 

docker-compose down



docker-compose exec postgres psql --username=postgres --dbname=postgres

Network db_postgres_default 

pre-commit run --all-files

docker build . -t okkam_api  

docker run -p 80:80 okkam_api  

docker run -p 80:80 --network db_postgres_default --name okkam okkam_api

docker network create okkam-net
docker network rm okkam-net    

docker network connect okkam-net okkam_api

docker network connect db_postgres_default api_okkam


docker inspect db_okkam | grep '"IPAddress"' | head -n 1

docker inspect <containerNameOrId>

docker network ls