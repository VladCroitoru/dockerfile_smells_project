FROM golang:1.9.0 AS builder
WORKDIR /go/src/github.com/alcheagle/rpi-prometheus-temp-exporter
COPY . .
RUN go get -d -v
RUN CGO_ENABLED=0 GOOS=linux GOARCH=arm go build

FROM scratch
COPY --from=builder /go/src/github.com/alcheagle/rpi-prometheus-temp-exporter .
ENTRYPOINT ["/rpi-prometheus-temp-exporter"]
