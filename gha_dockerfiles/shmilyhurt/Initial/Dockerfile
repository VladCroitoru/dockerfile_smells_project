FROM docker.io/golang:1.15.14 as builder
COPY .  /
WORKDIR /Initial
ENV GO111MODULE=on \
GOPROXY=https://goproxy.cn,direct
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o app main.go
RUN mkdir publish && cp app publish && \
    cp -r docs publish
FROM alpine
WORKDIR /Initial
COPY --from=builder /Initial/app .
ENV GIN_MODE=release \
PORT=8880
EXPOSE 8880
ENTRYPOINT ["./app"]


