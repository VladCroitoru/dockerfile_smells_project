FROM golang:1.15 as builder

WORKDIR $GOPATH/src/github.com/sylr/alertmanager-splunkbot

RUN apt-get update && apt-get dist-upgrade -y && apt-get install -y build-essential git

ADD . .

RUN go version

RUN git update-index --refresh; true
RUN CGO_ENABLED=0 go build -ldflags "-extldflags '-static' -w -s -X main.version=$(git describe --dirty --broken)"

# -----------------------------------------------------------------------------

FROM scratch

WORKDIR /usr/local/bin

COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group
COPY --from=builder /etc/services /etc/services
COPY --from=builder "/go/src/github.com/sylr/alertmanager-splunkbot/alertmanager-splunkbot" .

ENTRYPOINT ["/usr/local/bin/alertmanager-splunkbot"]
