FROM golang:latest
WORKDIR /build
COPY . .
RUN CGO_ENABLED=0 GOOS=linux make

FROM scratch
COPY --from=0 /build/autotransfer /autotransfer
COPY --from=0 /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
ENTRYPOINT ["/autotransfer"]
