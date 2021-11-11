FROM golang:alpine

WORKDIR /go/src/admin_go

COPY . .

EXPOSE 8080
RUN go generate && go build -o admin_go .


