FROM nginx:alpine
MAINTAINER Ruben Vermeersch <ruben@rocketeer.be>

ADD nginx.conf.tpl /etc/nginx/nginx.conf.tpl
ADD main.go /gopath/src/github.com/rubenv/nginx-static/
RUN apk add --update --virtual build-deps go git musl-dev && \
    export GOPATH=/gopath && \
    go get -v -t github.com/rubenv/nginx-static && \
    go install -ldflags '-w -s' -v github.com/rubenv/nginx-static && \
    apk del build-deps && \
    mv $GOPATH/bin/nginx-static /usr/bin/ && \
    rm -rf $GOPATH && \
    rm -rf /var/cache/apk/*

CMD ["nginx-static"]
