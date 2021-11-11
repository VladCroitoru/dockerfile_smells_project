FROM golang:1.17-alpine3.14 as builder

WORKDIR /app
COPY . .

RUN go build  cmd/main.go

# Run the Go Binary in Alpine.
FROM alpine:3.14

WORKDIR /app
COPY --from=builder  app/main main
RUN chmod +x ./main

EXPOSE 8080

CMD ["./main"]