FROM golang:1.11.2-alpine3.8 AS builder
RUN apk add --no-cache build-base && \
 echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories && \
 echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
 echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
 apk add --no-cache upx
WORKDIR /build
COPY ts3_discord_bot.go .
RUN CGO_ENABLED=0 GOOS=linux go build\
 -a\
 -ldflags '-s -w'\
 -installsuffix cgo\
 -o ts3_discord_bot && \
 upx --ultra-brute -qq ts3_discord_bot && \
 upx -t ts3_discord_bot

FROM alpine:3.8
ARG BUILD_DATE
ARG VCS_REF
LABEL maintainer="Krutov Alexander <goozler@mail.ru>" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/goozler/ts3_discord_bot.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.0-rc.1" \
      org.label-schema.description="Send a notification to Discord when someone \
has connected or disconnected to a TeamSpeak3 server"

RUN apk add --no-cache -q ca-certificates tzdata
WORKDIR /app
COPY wait-for .
COPY --from=builder /build/ts3_discord_bot .
CMD ["./ts3_discord_bot"]
