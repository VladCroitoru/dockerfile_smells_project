FROM golang:1.16-alpine

RUN apk update && apk add git

WORKDIR /app

COPY go.mod ./
COPY go.sum ./

RUN go mod download

COPY *.go ./
COPY core/ ./core/
COPY plugins/ ./plugins/

RUN go build -o /app/bundle-server

EXPOSE 8085

ENTRYPOINT [ "/app/bundle-server" ]
CMD ["server", "start"]