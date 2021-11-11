FROM bitnami/node:7.10.0-r1
MAINTAINER Miguel Martinez <migmartri@gmail.com>

COPY . /app
WORKDIR /app

RUN npm install

CMD ["node", "server.js"]
