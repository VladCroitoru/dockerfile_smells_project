FROM golang:1.17-alpine as builder

WORKDIR /app

COPY . .

RUN go mod download

RUN go build -o /Go-server server/main.go

# Creating server container
FROM alpine:3.13.6

COPY --from=builder /Go-server /Go-server

EXPOSE 3000

CMD ["/Go-server"]
