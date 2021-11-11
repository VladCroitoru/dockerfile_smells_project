FROM golang:latest as builder

RUN apt update
RUN apt install ca-certificates && update-ca-certificates
ENV GO111MODULE=on

WORKDIR /app

COPY go.mod ./
COPY go.sum ./

RUN go mod download

COPY . .

RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o ./bin/main .

FROM scratch

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /app/bin/main .
EXPOSE 3000

# Run executable
CMD ["./main"]