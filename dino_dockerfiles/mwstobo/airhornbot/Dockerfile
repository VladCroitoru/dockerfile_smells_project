FROM golang:1.11-alpine

WORKDIR /opt/airhornbot
COPY . .

RUN apk update \
 && apk add --no-cache \
            --virtual build \
            gcc \
            git \
            musl-dev

RUN go mod vendor \
 && go build cmd/bot/bot.go \
 && apk del build

CMD ["./bot", "-t YOUR_TOKEN_HERE"]
