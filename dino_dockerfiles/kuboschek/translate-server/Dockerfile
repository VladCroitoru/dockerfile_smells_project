FROM golang:1-alpine
LABEL maintainer="Leonhard Kuboschek <leo@kuboschek.me>"

RUN apk add --no-cache --no-progress git

WORKDIR /go/src/translate-server
COPY . .

RUN go get -v -d ./...
RUN go install -v ./...

EXPOSE 8080
CMD ["translate-server"]