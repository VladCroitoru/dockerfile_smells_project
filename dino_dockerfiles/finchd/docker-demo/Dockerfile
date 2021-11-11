FROM ubuntu:15.04
# From here we load our application's code in, therefore the previous docker
# "layer" thats been cached will be used if possible
ADD ./webapp /opt/webapp
WORKDIR /opt/webapp
RUN apt-get update -yq && apt-get upgrade -yq && apt-get install -yq curl git vim
RUN curl -sL https://deb.nodesource.com/setup | bash - && apt-get install -yq nodejs build-essential
RUN npm install -g npm
RUN npm config set registry http://registry.npmjs.org/
RUN npm install -g express@2.5.1
RUN npm install express
RUN npm install
EXPOSE 3000
