# syntax=docker/dockerfile:1

FROM golang:1.17.1-alpine3.14

WORKDIR /app

COPY . .

# RUN go mod download

RUN go build -o todo-app .

# EXPOSE 8080

CMD [ "/app/todo-app" ]

