# Build
FROM golang:buster as builder

#ENV GOPROXY=https://goproxy.cn

WORKDIR /app

COPY . .

RUN CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64 \
    go build -o MiraiGo-DD .


# Run
FROM debian:buster as runner

WORKDIR /app

COPY --from=builder /app/MiraiGo-DD .
COPY device.json .
COPY *.yaml .

ENTRYPOINT ["./MiraiGo-DD"]