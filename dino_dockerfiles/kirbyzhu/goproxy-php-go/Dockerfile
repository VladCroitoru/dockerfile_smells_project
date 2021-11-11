FROM golang:alpine
RUN apk add --no-cache curl && \
    curl -L "https://github.com/phuslu/goproxy/archive/server.php-go.tar.gz" | gzip -d | tar xv && \
    cd goproxy-server.php-go && \
    sed -i "s#123456#2Q43D9xVyQAOuvc7Iwjm#" index.go && \
    env CGO_ENABLED=0 && \
    go build -v -ldflags="-s -w" -o /goproxy-php

EXPOSE 8080
ENTRYPOINT /goproxy-php