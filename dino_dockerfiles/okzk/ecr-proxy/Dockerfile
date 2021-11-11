FROM golang AS build-env
ADD *.go Gopkg.* /go/src/github.com/okzk/ecr-proxy/
RUN go get -v github.com/golang/dep/cmd/dep \
  && cd /go/src/github.com/okzk/ecr-proxy/ && dep ensure -v \
  && CGO_ENABLED=0 go install -v github.com/okzk/ecr-proxy

FROM alpine
RUN apk add --no-cache ca-certificates
COPY --from=build-env /go/bin/ecr-proxy /usr/local/bin/
EXPOSE 5000
CMD ["ecr-proxy"]
