FROM golang:1.9-alpine3.7 as builder
ENV JOURNEY_VERSION v0.2.0

RUN apk update && apk add -y build-base git
RUN go get github.com/kabukky/journey && \
  cd $GOPATH/src/github.com/kabukky/journey && \
  git checkout ${JOURNEY_VERSION} && \
  git submodule update --init --recursive && \ 
  GOARCH=amd64 GOOS=linux go build && \
  mkdir /app && cp -r $GOPATH/src/github.com/kabukky/journey/journey $GOPATH/src/github.com/kabukky/journey/content $GOPATH/src/github.com/kabukky/journey/built-in $GOPATH/src/github.com/kabukky/journey/config.json /app

FROM alpine:3.7
WORKDIR /app
VOLUME /app

ENV PORT 8084
EXPOSE 8084

COPY --from=builder /app /app
CMD ["./journey"]