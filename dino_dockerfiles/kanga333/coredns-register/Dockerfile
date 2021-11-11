# go build image
FROM golang:alpine as build
RUN mkdir -p /go/src/github.com/kanga333/coredns-register
COPY . /go/src/github.com/kanga333/coredns-register
WORKDIR /go/src/github.com/kanga333/coredns-register
RUN go build .

# runtime image
FROM alpine
RUN apk add --no-cache tini
RUN mkdir -p /app
WORKDIR /app
COPY --from=build /go/src/github.com/kanga333/coredns-register/coredns-register /app/
COPY config.yml /app

ENV INTERVAL 60
ENV BASEPATH /skydns

ENTRYPOINT ["/sbin/tini", "--"]
CMD [ "/app/coredns-register", "-config", "/app/config.yml"]