FROM alpine:latest

RUN apk add -U aria2 && \
  rm -rf /var/cache/apk/* && \
  mkdir -p /app && \
  mkdir -p /app/download
    
ADD aria2.conf /app/aria2.conf

WORKDIR /app
VOLUME ["/app/download"]

EXPOSE 6800
ENTRYPOINT ["aria2c", "--conf-path=/app/aria2.conf"]
