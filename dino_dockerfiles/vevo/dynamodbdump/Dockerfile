FROM golang:alpine as base

# the base image is only used for compilation
ARG BUILD_VERSION=0.0.1-test
ENV CGO_ENABLED=0
ENV GOOS=linux
ENV GOARCH=amd64
ENV GO111MODULE=on
RUN apk add --no-cache git

WORKDIR /dynamodbdump
COPY . ./
RUN go test -v ./... && go vet ./... && go build

# Getting a small image with only the binary
FROM scratch
COPY --from=base /dynamodbdump/dynamodbdump /dynamodbdump
# This is needed when you do HTTPS requests
COPY --from=base /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
CMD ["/dynamodbdump"]
