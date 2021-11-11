FROM golang:1.15

WORKDIR /go/src/app
COPY ./go.mod ./go.mod
COPY ./go.sum ./go.sum
RUN go get -d -v ./...
COPY ./main.go ./main.go
COPY ./server ./server

RUN GOOS=`uname| tr '[:upper:]' '[:lower:]'` GOARCH=amd64 go build -o build

CMD ["./build"]
