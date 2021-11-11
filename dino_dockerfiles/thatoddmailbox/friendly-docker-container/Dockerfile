FROM ubuntu:14.04
RUN apt-get update

RUN apt-get install -y build-essential
RUN apt-get install -y libfreetype6 libfreetype6-dev libsqlite3-0 libsqlite3-dev libluajit-5.1-dev libluajit-5.1.2 libsdl2-2.0-0 libsdl2-dev libicu52 libicu-dev
RUN apt-get install -y g++-4.8 cmake

RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -
RUN apt-get install -y nodejs npm
RUN npm install -g azure-cli
