FROM node:4.1.1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install
COPY . /usr/src/app

ENV PORT=80
EXPOSE 80

ENTRYPOINT AMQP_URL=amqp://$RABBITMQ_PORT_5672_TCP_ADDR:$RABBITMQ_PORT_5672_TCP_PORT \
           exec npm start
