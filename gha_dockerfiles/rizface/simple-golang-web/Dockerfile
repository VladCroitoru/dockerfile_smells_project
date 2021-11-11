FROM golang:alpine

WORKDIR /app

COPY . .

RUN go mod download
RUN go build -o main main.go

CMD ["/app/main"]