FROM golang:latest as builder

RUN CGO_ENABLED=0 GOOS=linux go get -u github.com/golang/dep/cmd/dep

FROM alpine/git:latest

RUN apk --no-cache add ca-certificates
COPY --from=builder /go/bin/dep /usr/local/bin/
ADD entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
ENV GOPATH=/go

ENTRYPOINT [ "entrypoint.sh" ]
