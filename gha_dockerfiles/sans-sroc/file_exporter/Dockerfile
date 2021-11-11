# Stage 1 - Go, Build the Binary
FROM golang:1.17.3 as go-builder
WORKDIR /src/file_exporter
ENV GO111MODULE=on
COPY . /src/file_exporter
ARG branch=master
ENV BRANCH=${branch}
RUN make release && cp release/file_exporter /go/bin/file_exporter

# Stage 2 - Download Binaries
FROM appropriate/curl as binaries
ENV TINI_VERSION v0.18.0
RUN curl --fail -sLo /tini https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-static-amd64

# Stage X - Final Image
FROM debian:stretch-slim
ENTRYPOINT ["/usr/bin/tini", "--", "/usr/bin/file_exporter"]

RUN apt-get update && apt-get install -y ca-certificates liblz4-1 && rm -rf /var/lib/apt/lists/*
RUN useradd -r -u 999 -d /home/file_exporter file_exporter

COPY --from=binaries /tini /usr/bin/tini
COPY --from=go-builder /go/bin/file_exporter /usr/bin/file_exporter
RUN chmod +x /usr/bin/tini /usr/bin/file_exporter

USER file_exporter
