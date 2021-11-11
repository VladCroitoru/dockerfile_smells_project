FROM alpine

ADD https://github.com/sequenceiq/cbdproxy/releases/download/v0.0.9/cbdproxy_linux /bin/cbdproxy
RUN chmod +x /bin/cbdproxy

ENV PORT 80
ENTRYPOINT ["/bin/cbdproxy"]
