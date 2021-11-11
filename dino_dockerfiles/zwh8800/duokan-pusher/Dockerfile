FROM golang:1.8.1-alpine
MAINTAINER zwh8800 <496781108@qq.com>

WORKDIR /app

ENV LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

RUN apk update && apk add ca-certificates && apk add git && \
    apk add tzdata && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && go get -v github.com/Masterminds/glide

ADD . $GOPATH/src/github.com/zwh8800/duokan-pusher/

RUN cd $GOPATH/src/github.com/zwh8800/duokan-pusher/ && glide install && go install

VOLUME /app/config
VOLUME /app/data

CMD ["duokan-pusher", "-config", "/app/config/duokan.toml"]
