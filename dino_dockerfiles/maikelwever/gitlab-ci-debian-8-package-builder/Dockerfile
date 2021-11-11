FROM debian:jessie
RUN echo -n "deb http://cdn.debian.net/debian/ jessie main\ndeb http://security.debian.org/ jessie/updates main\ndeb http://cdn.debian.net/debian/ jessie-updates main" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y install git dh-make build-essential
