FROM golang:1.7.0-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache git

RUN go get github.com/docker/engine-api/client
RUN go get github.com/docker/engine-api/types
RUN go get github.com/docker/engine-api/types/container

RUN mkdir /app 
ADD . /app/ 
WORKDIR /app 

RUN go build -o main .

EXPOSE 3000

ENTRYPOINT ["/app/main"]