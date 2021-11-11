FROM golang:1.14.1-alpine3.11
MAINTAINER Nathan Sullivan <nathan@nightsys.net>
RUN apk add --no-cache git
WORKDIR /go/src/app
COPY *.go ./
RUN go get -d -v ./...
RUN go install -v ./...

# This image is like 13MB exported... :)
FROM alpine:3.11
WORKDIR /root/
COPY --from=0 /go/bin/app ./ec2-mock
EXPOSE 33333
CMD ["./ec2-mock"]
