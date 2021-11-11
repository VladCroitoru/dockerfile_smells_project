# Stage 1
FROM golang:1.17-alpine AS builder
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN go clean --modcache
RUN go build -o main

# Stage 2
FROM alpine:3.14
WORKDIR /root/
COPY --from=builder /app/config.json .
COPY --from=builder /app/main .
EXPOSE 8080
CMD ["./main"]