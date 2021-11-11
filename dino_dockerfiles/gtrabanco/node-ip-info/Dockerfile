FROM node:7-slim


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD . /usr/src/app/
RUN npm install
RUN ./node_modules/.bin/gulp ts

RUN mkdir /data && touch /data/cron-updateIPDatabase.log
ADD crontab /etc/cron.d/updateipdb
RUN chmod 0644 /etc/cron.d/updateipdb

EXPOSE 3280

CMD [ "npm", "start" ]