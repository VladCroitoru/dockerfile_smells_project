FROM golang:alpine

# install realize
RUN apk --no-cache add --virtual build-dependencies git
RUN apk --no-cache add gcc musl-dev
RUN go get github.com/tockins/realize

# install dockerize
RUN apk add --no-cache openssl
ENV DOCKERIZE_VERSION v0.6.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz