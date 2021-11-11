FROM golang:latest as builder
WORKDIR /go/src/github.com/TrilliumIT/gh-latest
COPY gh-latest.go .
RUN CGO_ENABLED=0 go build -a --installsuffix cgo --ldflags="-s" -o gh-latest


FROM alpine
RUN apk --no-cache add ca-certificates
COPY --from=builder /go/src/github.com/TrilliumIT/gh-latest .

EXPOSE 8080

CMD ["/gh-latest"]
