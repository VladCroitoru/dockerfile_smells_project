FROM golang:1.17 as build
WORKDIR /otel
COPY . .
RUN rm -rf build/*
RUN make build

FROM debian:stretch-slim
WORKDIR /otel
RUN apt-get update && apt-get install -y ca-certificates
COPY --from=build /otel/build/otelcompcol_linux_amd64 otelcompcol
CMD [ "/otel/otelcompcol" ]
