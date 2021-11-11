FROM frolvlad/alpine-glibc:alpine-3.5

MAINTAINER mrbillington

ENV VERSION=0.15.21

ADD https://www.factorio.com/get-download/${VERSION}/headless/linux64 /tmp/factorio_headless_x64.tar.xz
RUN tar xf /tmp/factorio_headless_x64.tar.xz && rm /tmp/factorio_headless_x64.tar.xz

VOLUME ["/config"]

EXPOSE 34197/udp

RUN mkdir /files
COPY map-gen-settings.example.json server-settings.example.json /files/

COPY start.sh /

CMD ["./start.sh"]
