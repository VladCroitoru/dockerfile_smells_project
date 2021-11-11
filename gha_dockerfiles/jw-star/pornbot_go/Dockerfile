FROM golang:alpine as builder
COPY . /app
WORKDIR /app
RUN go mod tidy
RUN CGO_ENABLED=0  go build -o main


FROM alpine

MAINTAINER jw-star


RUN apk add --no-cache tzdata  chromium  ffmpeg && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del tzdata && \
    rm -rf /var/cache/apk/* /tmp/* /var/tmp/* $HOME/.cache
RUN mkdir /config
COPY --from=builder /app/dictionary.txt  /app/stop_word.txt /app/stop_tokens.txt /app/main /app/md2.js  /home/

WORKDIR /home

CMD ["/home/main"]
