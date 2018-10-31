docker pull redis

docker build -t flask_service .

docker run -d -p 4000:3000 --name flask_app flask_service

docker stop flask_app

Screenshot of redis counter not working

docker run -d --name redis redis

docker run -d -p 4000:3010 --name flask_app --link redis:redis flask_service

screenshot of redis counter

cd part2/nginx/

docker build -t nginx_service .

cd part2/postgres/

docker build -t postgres_service .

cd part2/

docker build -t django_service .

docker-compose up or docker-compose -d up