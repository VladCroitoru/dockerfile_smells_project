FROM golang:latest
MAINTAINER Mattia Scalvini <matsca09@gmail.com>

COPY run.sh /run.sh
RUN useradd builder && mkdir /output && chown builder: /output

VOLUME /output
USER builder
ENTRYPOINT ["/run.sh"]
