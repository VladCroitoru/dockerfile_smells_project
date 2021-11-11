FROM golang:1.6

ENV APP_PKG_DIR /go/src/github.com/szpakas/fakepushprovider
RUN mkdir -p $APP_PKG_DIR
WORKDIR $APP_PKG_DIR
COPY ./ $APP_PKG_DIR/

RUN mkdir -p /srv

RUN go get -u github.com/govend/govend
RUN govend -v

RUN go build -v -o server ./cmd/server/main.go \
    && mv ./server /srv/

RUN go build -v -o test-gcmhttp ./cmd/test-gcmhttp/main.go && mv ./test-gcmhttp /srv/

RUN go build -v -o generator ./cmd/generator/main.go && mv ./generator /srv/

ENTRYPOINT ["/srv/server"]
