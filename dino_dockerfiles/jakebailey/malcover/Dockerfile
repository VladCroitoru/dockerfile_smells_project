FROM golang:alpine as builder

COPY . /go/src/app

RUN go install -v -ldflags="-s -w" app


FROM alpine

RUN apk --no-cache add ca-certificates

COPY --from=builder /go/bin/app /bin/app

EXPOSE 5000
CMD ["/bin/app"]
