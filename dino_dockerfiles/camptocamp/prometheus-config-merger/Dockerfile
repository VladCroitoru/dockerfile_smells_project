FROM golang:1.13 as builder
WORKDIR /go/src/github.com/camptocamp/prometheus-config-merger/
COPY main.go .
COPY Makefile .
RUN go get
RUN make prometheus-config-merger

FROM scratch
COPY --from=builder /go/src/github.com/camptocamp/prometheus-config-merger/prometheus-config-merger /
ENTRYPOINT ["/prometheus-config-merger"]
VOLUME [ "/etc/prometheus" ]
CMD [""]
