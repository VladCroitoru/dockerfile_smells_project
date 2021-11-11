FROM node:6.2.2

MAINTAINER Enrique Garcia Navalon "garcianavalon@syncrtc.com"

WORKDIR /app

# nodemon for live reloading in development
RUN npm install -gq nodemon

# use changes to package.json to force Docker not to use the cache
# when we change our application's nodejs dependencies:
COPY package.json ./
RUN npm install -q

# From here we load our application's code in, therefore the previous docker
# "layer" thats been cached will be used if possible
COPY . /app

EXPOSE 3000

# MUST be the name of the mongo service in docker-compose.yml.
# More info: https://docs.docker.com/compose/networking/
ENV MONGO_HOST='mongo'

CMD [ "npm", "start" ]