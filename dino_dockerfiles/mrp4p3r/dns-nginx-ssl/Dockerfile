FROM alpine:3.7

RUN apk update && apk add nano
ENV EDITOR nano

RUN apk add --no-cache openssl socat curl && \
    apk add --no-cache nginx pdns pdns-backend-sqlite3 && \
    rm -rf /root/.cache

RUN apk add --no-cache --virtual .deps git && \
    git clone https://github.com/Neilpang/acme.sh.git /src/acme.sh && \
    cd /src/acme.sh && ./acme.sh --install && cd - \
    rm -rf /src/acme.sh && \
    apk del .deps

COPY ./src /src/manage

RUN apk add --no-cache --virtual .deps \
        build-base linux-headers \
        libc-dev libstdc++ libgcc \
        gcc g++ make git && \
    mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 && \
    curl https://storage.googleapis.com/golang/go1.9.1.linux-amd64.tar.gz | tar xzf - -C /usr/local/ && \
    \
    export GOROOT=/usr/local/go && \
    export GOPATH=/gopath && \
    export GOBIN=/gopath/bin && \
    export CGO_ENABLED=0 && \
    export PATH=$PATH:$GOROOT/bin:$GOPATH/bin && \
    \
    echo Building github.com/immortal/immortal && \
    mkdir /tmp/gopath && \
    GOPATH=/tmp/gopath go get -u github.com/immortal/immortal && \
    cd /tmp/gopath/src/github.com/immortal/immortal && \
    GOPATH=/tmp/gopath make install && cd - && \
    rm -rf /tmp/gopath && \
    \
    echo Building ./src/manage.go && \
    cd /src/manage && mkdir gopath && \
    GOPATH=$PWD/gopath go get && \
    GOPATH=$PWD/gopath go build manage.go && \
    cp manage /usr/local/bin && \
    cd / && rm -rf /src/manage && \
    \
    rm -rf /usr/local/go && \
    apk del .deps

RUN mkdir -p /run/nginx /var/www /etc/sslcerts && \
    chown nginx:nginx /run/nginx /var/www /etc/sslcerts && \
    rm -rf /etc/nginx/conf.d/* && \
    mkdir /var/pdns /etc/pdns/pdns.d && \
    chown pdns:pdns -R /var/pdns /etc/pdns/pdns.d


RUN echo 'daemon off;' >> /etc/nginx/nginx.conf
COPY ./confs/powerdns/pdns.conf /etc/pdns/pdns.conf
COPY ./confs/immortal/ /etc/immortal/
COPY ./scripts/ /scripts/

RUN chmod u+x /scripts/*
ENV PATH=$PATH:/scripts

VOLUME ["/var/pdns", "/etc/sslcerts", "/root/.acme.sh", "/etc/nginx/conf.d"]
EXPOSE 53 80 443

CMD ["start.sh"]
