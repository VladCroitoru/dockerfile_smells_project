FROM golang:1.16-alpine
WORKDIR /go/src/app
COPY go.mod .
COPY go.sum .
RUN go mod download
COPY . .
RUN go build -o ./out/app .
EXPOSE 8080
CMD ["./out/app"]