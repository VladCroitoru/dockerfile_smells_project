FROM golang:1.10
COPY ./protoc/bin/protoc /bin/protoc
COPY ./protoc/include /usr/local/include/
RUN go get github.com/AsynkronIT/protoactor-go/... &&\
    cd $GOPATH/src/github.com/AsynkronIT/protoactor-go &&\
    go get ./... &&\
    make
RUN echo 'deb http://deb.debian.org/debian testing main' >> /etc/apt/sources.list &&\
    apt -qq update &&\
    apt -y install -qq swig3.0 &&\
    apt -y install -qq -t testing g++ &&\
    apt -y autoremove &&\
    rm -rf /var/lib/apt/lists/* &&\
    ln -s /usr/bin/swig3.0 /usr/bin/swig
WORKDIR /go/src/github.com/rolevax/ih/
RUN go get github.com/fatih/camelcase &&\
    go get github.com/rolevax/sp4g &&\
    go get github.com/chzyer/readline &&\
    go get github.com/go-pg/pg &&\
    go get github.com/howeyc/gopass &&\
    go get github.com/emicklei/go-restful &&\
    go get github.com/dgrijalva/jwt-go &&\
    go get github.com/go-redis/redis &&\
    go get github.com/importcjj/sensitive &&\
    go get github.com/microcosm-cc/bluemonday

