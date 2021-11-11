FROM golang:1.17 AS builder

WORKDIR /go/src/app
COPY fullcycle.go .

RUN go build -o fullcycle fullcycle.go

FROM scratch

COPY --from=builder /go/src/app .

CMD ["./fullcycle"]
