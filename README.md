# GDG-DevFest Talk - "Dockerizing Python Microservices"

I and Ramanath R gave a talk on GDG-Hyd Devfest 2018 on "Dockerizing Python Microservices". This repo concist the code we had used for demo and below are the setup instructions along with some references. Please feel free to play around with these microservices and raise a PR if you find any issue or would like to add on something to the current setup.

### SetUp Part1

```sh
$ git clone https://github.com/inovizz/gdg-talk.git
$ cd gdg-talk
$ cd part1/
$ docker build -t flask_service .
$ docker run -d -p 4000:3010 --name flask_app flask_service
```
Screenshot of redis counter not working
![redis not setup](https://raw.githubusercontent.com/inovizz/gdg-talk/master/part1/woredis.png)
```sh
$ docker rm -f flask_app
$ docker pull redis
$ docker run -d --name redis redis
$ docker run -d -p 4000:3010 --name flask_app --link redis:redis flask_service
```
Screenshot of redis counter working
![redis not setup](https://raw.githubusercontent.com/inovizz/gdg-talk/master/part1/wredis.png)

### SetUp Part2
```sh
$ cd ../part2/nginx/
$ docker build -t nginx_service .
$ cd ../postgres
$ docker build -t postgres_service .
$ cd ../
$ docker build -t django_service .
$ docker-compose up or docker-compose -d up
```