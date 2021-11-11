FROM golang:1.13 AS builder
WORKDIR /go/src/github.com/carlpett/grafana-loader/
COPY . .
RUN make build

FROM scratch
EXPOSE 8080
USER 1000
ENTRYPOINT ["/grafana-loader"]
COPY --from=builder /go/src/github.com/carlpett/grafana-loader/grafana-loader /grafana-loader
