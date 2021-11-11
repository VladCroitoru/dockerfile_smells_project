FROM node:8-alpine
MAINTAINER Chris Schmich <schmch@gmail.com>
COPY crontab /var/spool/cron/crontabs/root
COPY /src /app
WORKDIR /app
RUN npm install
ENTRYPOINT ["/usr/sbin/crond", "-f"]
