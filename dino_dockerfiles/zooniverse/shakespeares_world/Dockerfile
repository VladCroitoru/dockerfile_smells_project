FROM node:9

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ARG NODE_ENV
COPY package*.json /usr/src/app/
RUN npm install && npm cache clean --force
COPY . /usr/src/app

ENV NODE_ENV production

CMD ["npm", "build"]
