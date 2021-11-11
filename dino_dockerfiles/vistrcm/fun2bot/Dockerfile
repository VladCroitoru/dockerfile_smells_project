# build application phase
FROM golang:1.11 as builder

WORKDIR /go/src/github.com/vistrcm/fun2bot
COPY ./ .

## handle dependencies
RUN echo "installing deps" \
    && go get -v -u github.com/golang/dep/cmd/dep\
    && dep ensure -v

# build with specific params to avoid issues of running in alpine
RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -v -a -o fun2bot .

# build image
FROM alpine:latest
RUN apk --no-cache add ca-certificates
COPY --from=builder /go/src/github.com/vistrcm/fun2bot/fun2bot /fun2bot
# array in etrypoint is a dirty hack to be able to pass parameters via CMD later
ENTRYPOINT ["/fun2bot"]
