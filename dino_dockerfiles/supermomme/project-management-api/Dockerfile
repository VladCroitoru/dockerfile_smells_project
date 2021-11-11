FROM node:7.5.0

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV
COPY package.json /usr/src/app/
RUN npm install --unsafe-perm  && npm cache clean
RUN mkdir worker
COPY . /usr/src/app

VOLUME ["/usr/src/app/data"]
EXPOSE 80


CMD [ "npm", "start" ]
