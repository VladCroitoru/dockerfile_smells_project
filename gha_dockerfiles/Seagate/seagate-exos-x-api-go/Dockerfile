FROM golang:1.15-alpine

RUN apk add --update git curl g++

COPY . /app

WORKDIR /app

ENTRYPOINT [ "/bin/sh" ]

RUN go mod download

CMD [ "-c", "sleep 1 && go test" ]
