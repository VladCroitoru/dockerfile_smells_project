### Bulder
FROM golang:1.15.11-alpine3.13
RUN apk update
RUN apk add --no-cache tzdata

WORKDIR /usr/src/app

COPY go.mod .
COPY go.sum .

RUN go mod tidy
# install dependencies

COPY . .

RUN GO111MODULE=on CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -ldflags="-s -w" -o main main.go;

EXPOSE 8080

ENTRYPOINT ["./main"]