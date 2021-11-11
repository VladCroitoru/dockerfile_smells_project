FROM golang:1.17 as builder
WORKDIR /go/src/faxxr
COPY . .
RUN go version
RUN CGO_ENABLED=0 GOOS=linux GO111MODULE=on go install
RUN mkdir -p /home/.config/pdfcpu/fonts

FROM ancientlore/goimg:latest

# needed for pdfcpu
COPY --from=builder /home/.config /home/.config

COPY --from=builder /go/bin/faxxr /usr/bin/faxxr
COPY --from=builder /go/src/faxxr/media /faxxr/media
COPY --from=builder --chown=nonroot:nonroot /go/src/faxxr/tmp /faxxr/tmp

EXPOSE 9000/tcp
WORKDIR /faxxr
ENTRYPOINT ["/usr/bin/faxxr"]
