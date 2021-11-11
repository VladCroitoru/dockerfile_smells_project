FROM golang:latest

RUN mkdir -p /go/src/app
WORKDIR /go/src/app
COPY . /go/src/app/
RUN go get -v -d \
  && CGO_ENABLED=0 GOOS=linux go install -a -installsuffix cgo app

FROM alpine:latest
MAINTAINER Mark Watson <markwatsonatx@gmail.com>
COPY --from=0 /go/bin/app /app
CMD ["/app", "80"]