FROM golang:1.15 AS builder

ENV CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64 \
    GIT_TERMINAL_PROMPT=1

COPY ./main.go ${GOPATH}/src/github.com/kvendingoldo/echo-http-server/main.go
WORKDIR ${GOPATH}/src/github.com/kvendingoldo/echo-http-server
RUN go build -ldflags="-s -w" -o server .

FROM scratch
COPY --from=builder go/src/github.com/kvendingoldo/echo-http-server/server /app/
WORKDIR /app
EXPOSE 8080
ENTRYPOINT ["/app/server"]