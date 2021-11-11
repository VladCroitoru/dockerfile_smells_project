#dockerfile

#using official node LTS repo
FROM node:7.0.0
MAINTAINER Jujhar Singh <jujhar@jujhar.com>

#RUN npm install supervisor -g

#environment variables
ENV NODE_PORT 8080
ENV NODE_ENV development
ENV LOG_PATH /var/log
ENV LOG_LEVEL info
ENV SUPPRESS_NO_CONFIG_WARNING yes-potatos

ADD app /app

#this is the root folder we'll work from
WORKDIR /app

#entrypoint
ENTRYPOINT ["node", "index.js"]