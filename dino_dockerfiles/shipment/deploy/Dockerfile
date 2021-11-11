FROM ubuntu:trusty

#GIT
RUN apt-get update && \
      apt-get install -y git curl

#NODE
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - && \
      apt-get install -y nodejs

#DOCKER
RUN curl -sSL https://get.docker.com/ | sed 's/docker-engine/docker-engine=1.10.3-0~trusty/' | sh

ENV NODE_ENV production

#NODEMON
RUN npm i -g nodemon

#SETUP
RUN mkdir -p /repos

#APP
ADD package.json /app/
RUN cd /app && npm install --silent
ENV PATH /app/node_modules/.bin:$PATH

ADD . /app/server
WORKDIR /app/server

CMD ["npm", "start"]
