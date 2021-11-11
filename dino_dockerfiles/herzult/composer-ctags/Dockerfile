FROM alpine:latest

RUN apk update && apk add inotify-tools ctags

RUN mkdir /app

WORKDIR /app

COPY ctags /.ctags

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT /entrypoint.sh
