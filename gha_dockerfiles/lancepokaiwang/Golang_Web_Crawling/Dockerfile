FROM golang:1.16-alpine

WORKDIR /app

RUN apk update
RUN apk add git

COPY . /app

RUN go mod tidy
RUN go build -o /docker-gs-ping

EXPOSE 8000

CMD [ "/docker-gs-ping" ]