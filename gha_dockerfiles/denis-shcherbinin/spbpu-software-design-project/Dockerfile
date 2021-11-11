FROM golang:1.17-alpine3.13 as builder

COPY ./ /go/src/todo-app

WORKDIR /go/src/todo-app/cmd/todo-app

RUN go version && go install

FROM alpine:3.13

COPY --from=builder /go/bin/todo-app /srv/todo-app

WORKDIR /srv

CMD ["/srv/todo-app"]
