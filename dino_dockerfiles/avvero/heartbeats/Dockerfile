FROM golang:latest
LABEL maintainer avvero

ADD . /app
WORKDIR /app
RUN go get github.com/stretchr/stew
RUN go get github.com/stretchr/signature
RUN go build -o main .
CMD ["/app/main", "-httpPort=8111", "-infoUpdateInterval=5", "-heraldEndpoint=https://f2g.site/bot/herald/api/message"]

EXPOSE 8111
