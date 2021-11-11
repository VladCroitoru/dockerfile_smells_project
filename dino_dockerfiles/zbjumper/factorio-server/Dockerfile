FROM yoojia/ubuntu:14.04

MAINTAINER zbjumper <zbjumper@gmail.com>

ADD factorio_headless_x64_0.14.20.tar.gz /

WORKDIR /factorio

ADD start.sh ./

RUN chmod +x start.sh

VOLUME ["/factorio/saves"]

EXPOSE 34197/udp

ENTRYPOINT ["./start.sh"]
