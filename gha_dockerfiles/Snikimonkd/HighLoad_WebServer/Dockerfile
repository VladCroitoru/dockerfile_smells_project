FROM ubuntu:latest
EXPOSE 8080
ADD . /opt/app
WORKDIR /opt/app
RUN apt-get update && apt-get -y install gcc
RUN gcc -pthread -o rofl main.c
COPY . .
CMD ./main.o