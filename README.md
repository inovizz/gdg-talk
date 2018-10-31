# GDG-DevFest Talk - "Dockerizing Python Microservices"

I and Ramanath R gave a talk on GDG-Hyd Devfest 2018 on "Dockerizing Python Microservices". This repo concist the code we had used for demo and below are the setup instructions along with some references. Please feel free to play around with these microservices and raise a PR if you find any issue or would like to add on something to the current setup.

### SetUp Part1 (DockerFile)

This part dockerize a basic flask service, which is trying to communicate with redis and update the counter however, since once you build this image and run the container, the redis counter value wouldn't be updated as container doesn't have setup or link to redis host.

```sh
$ git clone https://github.com/inovizz/gdg-talk.git
$ cd gdg-talk
$ cd part1/
$ #build the image, flask_service is the image name here
$ docker build -t flask_service .
$ # run the container, map port 4000(host) to 3010(guest) and give a container name - flask_app
$ docker run -d -p 4000:3010 --name flask_app flask_service
```
Follow the above steps and try to see the output on browser, hit http://localhost:4000/. Here is the response which you will see after making a request to flask_service container.

<p align="left">
![redis not setup](https://raw.githubusercontent.com/inovizz/gdg-talk/master/part1/woredis.png)
</p>
We can see that connection to redis is not working let's try make redis host available for flask_app container.
For that let's irsrt remove the flask_app container and pull the redis image, start redis container and link it with flask_app container. Follow the below steps-
```sh
$ docker rm -f flask_app
$ docker pull redis
$ # below command runs a container of name redis and it also used an image called redis to instantiate it.
$ docker run -d --name redis redis
$ # below command links the redis container to to flask_app container.
$ docker run -d -p 4000:3010 --name flask_app --link redis:redis flask_service
```
After running above commands we can check the output of http://localhost:4000 on browser and this time redis counter shall be working, below is a screenshot for reference -

<p align="left">
![redis setup](https://raw.githubusercontent.com/inovizz/gdg-talk/master/part1/wredis.png)
</p>

### SetUp Part2 (Docker Compose)

This part contains a docker-compose file which has listed setup for few microservices, please note nginx and postgres are not being used by any other service in this demo. It is just been configured for the demo sake, also in order to run docker-compose file, we will have build separate images for nginx, postgres and django app, so please follow below instructions and in the end to check output from flask and django app, verify following endpoints -

http://localhost:8888
http://localhost

```sh
$ cd ../part2/nginx/
$ docker build -t nginx_service .
$ cd ../postgres
$ docker build -t postgres_service .
$ cd ../
$ docker build -t django_service .
$ docker-compose up or docker-compose -d up
```

Few reference links one can refer to read and understand more about docker and docker-compose.

- https://docker-curriculum.com
- Docker File reference -  https://docs.docker.com/engine/reference/builder/
- Docker Compose reference -  https://docs.docker.com/compose/compose-file/