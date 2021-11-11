FROM golang:latest

ENV APP_PKG_DIR /go/src/github.com/szpakas/example-go-messenger
RUN mkdir -p $APP_PKG_DIR

COPY ./ $APP_PKG_DIR/
WORKDIR $APP_PKG_DIR

RUN go get -u github.com/govend/govend
RUN govend -v

RUN mkdir -p /srv
RUN go build -v -o app . \
    && mv ./app /srv/

ENTRYPOINT ["/srv/app"]

EXPOSE 8080
