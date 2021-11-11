FROM golang:1.12.6-alpine3.9 AS build-env

RUN apk add --no-cache git gcc musl-dev
RUN apk add --update make
RUN go get github.com/google/wire/cmd/wire
WORKDIR /go/src/github.com/devtron-labs/git-sensor
ADD . /go/src/github.com/devtron-labs/git-sensor/
RUN GOOS=linux make

FROM alpine:3.9
COPY ./git-ask-pass.sh /git-ask-pass.sh
RUN chmod +x /git-ask-pass.sh
RUN apk add --no-cache ca-certificates
RUN apk add git --no-cache
RUN apk add openssh --no-cache
COPY --from=build-env  /go/src/github.com/devtron-labs/git-sensor/git-sensor .
CMD ["./git-sensor"]