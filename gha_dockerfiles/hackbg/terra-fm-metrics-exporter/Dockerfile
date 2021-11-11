FROM golang:1.16-alpine3.12 AS go-builder
RUN apk add build-base
WORKDIR /
COPY . .

ADD https://github.com/CosmWasm/wasmvm/releases/download/v0.16.0/libwasmvm_muslc.a /lib/libwasmvm_muslc.a
RUN sha256sum /lib/libwasmvm_muslc.a | grep ef294a7a53c8d0aa6a8da4b10e94fb9f053f9decf160540d6c7594734bc35cd6

RUN go build -mod=readonly -tags "muslc" -o bin/terra-chainlink-exporter

FROM alpine:3.12
RUN apk add ca-certificates
COPY --from=go-builder /bin/terra-chainlink-exporter /bin/terra-chainlink-exporter

EXPOSE 8089

ENTRYPOINT ["/bin/terra-chainlink-exporter"]
