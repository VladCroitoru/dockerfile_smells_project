# Builder
FROM golang:1.17-alpine AS builder
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN go mod tidy
RUN go build -o main

# Runner
FROM alpine:3.14
WORKDIR /app
COPY --from=builder /app/main .
EXPOSE 8000
CMD ["./main"]