FROM golang:latest 

MAINTAINER Yoan Rousseau / y0an , https://github.com/y0an

ENV RESULT_DIR=/rabbitmq-dump-queue-result

ENV RABBITMQ_LOGIN=admin
ENV RABBITMQ_PWD=admin
ENV RABBITMQ_HOST=localhost
ENV RABBITMQ_PORT=5672
ENV QUEUE_NAME=queue
ENV MAX_MESSAGE=50

RUN mkdir $RESULT_DIR

RUN go get github.com/dubek/rabbitmq-dump-queue

ENTRYPOINT rabbitmq-dump-queue -uri=amqp://$RABBITMQ_LOGIN:$RABBITMQ_PWD@$RABBITMQ_HOST:$RABBITMQ_PORT/ -queue=$QUEUE_NAME -max-messages=$MAX_MESSAGE -output-dir=$RESULT_DIR
