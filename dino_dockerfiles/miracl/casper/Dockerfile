FROM golang as builder
WORKDIR /go/src/github.com/miracl/casper/
COPY ./ .
RUN CGO_ENABLED=0 GOOS=linux go build -a -ldflags '-extldflags "-static" -w -s' ./cmd/casper

FROM scratch
COPY --from=builder /go/src/github.com/miracl/casper/casper .
ENTRYPOINT ["./casper"]
