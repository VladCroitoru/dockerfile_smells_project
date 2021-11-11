FROM alpine:3.7
LABEL maintainer="George Kutsurua <g.kutsurua@gmail.com>"

RUN apk add --no-cache nginx nginx-mod-http-lua nginx-mod-http-lua-upstream \
                       nginx-mod-devel-kit nginx-mod-http-set-misc \
                       lua openssl ca-certificates

RUN cd /tmp &&\
    wget https://github.com/bitly/oauth2_proxy/releases/download/v2.2/oauth2_proxy-2.2.0.linux-amd64.go1.8.1.tar.gz &&\
    tar -xzvf oauth2_proxy*.tar.gz &&\
    mv oauth2_proxy*/* /usr/sbin/ &&\
    rm -rf /tmp/* /var/cache/apk/*

ENTRYPOINT ["/usr/sbin/nginx"]
