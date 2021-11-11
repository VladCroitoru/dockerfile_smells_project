FROM golang:1.17 AS builder

WORKDIR /app

COPY go.mod .
COPY go.sum .

RUN go mod download

ADD . /app
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o /app/api .

FROM alpine

COPY --from=builder /app/api .
ENTRYPOINT ["./api"]
EXPOSE 8080