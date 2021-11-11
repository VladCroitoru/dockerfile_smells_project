FROM node:8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package* /usr/src/app/
RUN npm install --silent && npm cache clean --force
COPY . /usr/src/app

CMD [ "npm", "start" ]

EXPOSE 8080