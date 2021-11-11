FROM node:latest
MAINTAINER galan

RUN cd /tmp && \
    git clone https://github.com/RabbitMQSimulator/RabbitMQSimulator.git && \
    cd RabbitMQSimulator && \
    npm install

CMD node /tmp/RabbitMQSimulator/app.js

EXPOSE 3000/tcp

