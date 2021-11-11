FROM golang:1.17.1-alpine3.14

WORKDIR /go/src/github.com/dpattmann/furby

EXPOSE 8443

COPY . .

RUN apk add -U --no-cache curl jq

RUN cd /go/src/github.com/dpattmann/furby/cmd/furby ; go install

ENTRYPOINT [ "/bin/sh", "-c", "/go/src/github.com/dpattmann/furby/start.sh" ]
