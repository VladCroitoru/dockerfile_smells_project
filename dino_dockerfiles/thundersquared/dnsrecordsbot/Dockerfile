FROM golang:1.9 as builder
ADD . /src
RUN cd /src && go get -d && CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o bot .

FROM alpine:latest
ENV BOT_TOKEN=
RUN apk --no-cache add ca-certificates bind-tools
COPY --from=builder /src/bot .
ENTRYPOINT ./bot
