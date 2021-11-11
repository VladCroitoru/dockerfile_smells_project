FROM alpine:latest
RUN apk update && apk add ca-certificates wget && update-ca-certificates
RUN wget https://github.com/bitly/oauth2_proxy/releases/download/v2.1/oauth2_proxy-2.1.linux-amd64.go1.6.tar.gz && \
    tar zxf oauth2_proxy-2.1.linux-amd64.go1.6.tar.gz && \
    mv oauth2_proxy-2.1.linux-amd64.go1.6/oauth2_proxy /usr/bin && \
    rm -rf oauth2_proxy-2.1.linux-amd64.go1.6*
