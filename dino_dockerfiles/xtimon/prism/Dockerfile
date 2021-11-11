FROM debian:jessie

ENV VERSION=0.6.17

ADD https://github.com/stoplightio/prism/releases/download/v${VERSION}/prism_linux_amd64 /usr/bin/prism

RUN chmod +x /usr/bin/prism

ENTRYPOINT ["/usr/bin/prism"]

CMD ["--help"]
