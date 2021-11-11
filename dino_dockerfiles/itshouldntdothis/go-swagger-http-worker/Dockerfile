FROM golang:latest as builder

RUN go get github.com/tools/godep

WORKDIR /go/src/app

COPY Godeps/ Godeps/
RUN godep restore

COPY . .

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo .

FROM alpine:latest
RUN apk --no-cache add ca-certificates

WORKDIR /root/

COPY --from=builder /go/src/app/app .

CMD ["./app"]
