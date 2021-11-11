FROM node:14-buster

WORKDIR /usr/src/app

RUN apt update && apt upgrade -y

COPY . .

# 1- create image: docker build -t back-3 .
# 2- run container: docker run --rm -it --name backend-studies -v ${pwd}:/usr/src/app back-3 bash
