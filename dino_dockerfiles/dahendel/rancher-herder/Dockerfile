FROM golang:alpine as builder

RUN apk add --update --no-cache glide git && \
  go get -d github.com/dahendel/cattle-herder && \
  cd /go/src/github.com/dahendel/cattle-herder && \
  glide install -v && \
  go build

FROM alpine

COPY --from=builder /go/src/github.com/dahendel/cattle-herder/cattle-herder /usr/local/bin/

CMD /usr/local/bin/cattle-herder