FROM golang:1.9
WORKDIR /go/src/github.com/torch
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo


FROM prom/busybox:latest
COPY --from=0 /go/src/github.com/torch/torch /bin/torch
WORKDIR    /app
ENTRYPOINT [ "/bin/torch" ]
CMD        [ "--config.file=/etc/prometheus/config.yml" ]
