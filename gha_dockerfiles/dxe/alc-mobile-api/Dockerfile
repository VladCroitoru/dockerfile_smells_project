FROM golang:1.16.2-alpine3.13
RUN mkdir /app
ADD . /app
WORKDIR /app

RUN go get github.com/githubnemo/CompileDaemon

ENTRYPOINT CompileDaemon --build="go build -o alc-mobile-api ." --command=./alc-mobile-api
