FROM alpine:3.5

WORKDIR /unzip
ENTRYPOINT ["unzip"]
RUN apk add -U unzip && rm -rf /var/cache/apk/*
