FROM node:5.10

COPY docker/crontab /etc/cron.d/paphos-analytics

#RUN apt-get update  && apt-get install -y wget cron && chmod 0644 /etc/cron.d/paphos-analytics

RUN  mkdir /src && npm install nodemon bower gulp-cli -g && apt-get update && apt-get install -y cron wget && chmod 0644 /etc/cron.d/paphos-analytics

RUN wget https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-amd64-v0.2.0.tar.gz && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.2.0.tar.gz

COPY ./ /src
WORKDIR /src
RUN npm install && bower install --allow-root && NODE_ENV=production gulp

EXPOSE 5000

CMD dockerize -wait http://mongo:27017 -wait http://rabbitmq:15672 -timeout 60s cron && npm start
