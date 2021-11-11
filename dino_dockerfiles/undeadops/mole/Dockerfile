FROM golang:1.9-alpine
WORKDIR /go/src/github.com/undeadops/mole
COPY . /go/src/github.com/undeadops/mole/
RUN CGO_ENABLED=0 GOOS=linux go build -o mole api/*.go

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=0 /go/src/github.com/undeadops/mole/mole .
CMD ["./mole"]
