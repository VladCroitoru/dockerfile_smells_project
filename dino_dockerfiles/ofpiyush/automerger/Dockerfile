FROM golang:1.10.0 as builder

WORKDIR /go/src/github.com/ofpiyush/automerger/

ADD . .

RUN CGO_ENABLED=0 GOOS=linux go build -ldflags "-s" -a -installsuffix cgo -o ./deploy/files/automerger .

# Our users might not have volume mount capabilities
FROM alpine:3.7

RUN apk --no-cache add ca-certificates

COPY --from=builder /go/src/github.com/ofpiyush/automerger/deploy/files/automerger .

EXPOSE 3000

ENTRYPOINT ["./automerger"]