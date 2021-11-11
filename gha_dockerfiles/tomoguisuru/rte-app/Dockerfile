
FROM node:12.22.6

EXPOSE 4200 7357 9222

COPY . /app
WORKDIR /app

RUN npm install -q -g ember-cli

RUN npm install

ENTRYPOINT ember s -e production