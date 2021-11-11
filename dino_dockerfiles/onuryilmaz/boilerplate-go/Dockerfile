FROM golang:1.9 as tester
ADD . /go/src/github.com/onuryilmaz/boilerplate-go
WORKDIR /go/src/github.com/onuryilmaz/boilerplate-go
RUN go test -v ./...

FROM golang:1.9 as builder
ADD . /go/src/github.com/onuryilmaz/boilerplate-go/
WORKDIR /go/src/github.com/onuryilmaz/boilerplate-go/cmd
RUN GOOS=linux go build -o boilerplate-go

FROM ubuntu
COPY --from=builder /go/src/github.com/onuryilmaz/boilerplate-go/cmd/boilerplate-go /boilerplate-go
ENTRYPOINT ["./boilerplate-go"]