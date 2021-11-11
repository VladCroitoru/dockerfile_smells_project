FROM golang:1.11.5-alpine3.8
LABEL maintainer="Siddhartha Basu <siddhartha-basu@northwestern.edu>"
RUN apk add --no-cache git build-base
RUN mkdir -p /modware-identity
WORKDIR /modware-identity
COPY go.mod *.go ./
ADD server server
ADD commands commands
ADD message message
ADD validate validate
ADD storage storage
RUN go get ./... && go mod tidy && go build -o app

FROM alpine:3.8
RUN apk --no-cache add ca-certificates
COPY --from=0 /modware-identity/app /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/app"]
