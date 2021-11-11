FROM golang as builder

WORKDIR /go/src/app

COPY src .

RUN go build desafiogo.go

FROM scratch

COPY --from=builder /go/src/app .

ENTRYPOINT ["/desafiogo"]

