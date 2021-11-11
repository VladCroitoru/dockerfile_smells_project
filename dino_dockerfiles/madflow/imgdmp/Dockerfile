FROM node:14-alpine

ENV SUPERVISOR_VERSION=3.3.4

RUN apk update && apk add -u python py-pip
RUN pip install supervisor==$SUPERVISOR_VERSION

WORKDIR /app

COPY deployment/docker/supervisord.conf /etc/supervisord.conf

COPY package.json .
COPY yarn.lock .

RUN yarn install

COPY . .

EXPOSE 3000

ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]
