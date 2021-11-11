FROM golang:1.17 as go_builder

RUN mkdir /build
ADD . /build
RUN cd /build && \
    go mod download && \
    CGO_ENABLED=0 go build -o /build/citadel487-bot .


FROM ubuntu:focal as py_builder

ENV DEBIAN_FRONTEND noninteractive
RUN mkdir /build && \
    apt update && \
    apt install -y python3 python3-dev python3-pip python3-venv openssl

ADD downloader487/downloader/requirements.txt /build
ADD downloader487/downloader/setup.sh /build
RUN cd /build && ./setup.sh

ADD downloader487/downloader /build
RUN cd /build && ./build.sh


FROM ubuntu:focal

ENV DEBIAN_FRONTEND noninteractive

RUN mkdir -p /opt/app && \
    apt update && \
    apt install -y ca-certificates ffmpeg && \
    apt clean

COPY --from=go_builder /build/citadel487-bot /opt/app
COPY --from=py_builder /build/dist/downloader487 /opt/app

ENTRYPOINT [ "/opt/app/citadel487-bot", "--downloader-path", "/opt/app/downloader487" ]
