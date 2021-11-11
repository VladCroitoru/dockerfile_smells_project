FROM centos:7
MAINTAINER github.com/wnkz

ADD factorio_headless_x64_0.12.29.tar.gz /opt/
WORKDIR /opt/factorio

RUN /opt/factorio/bin/x64/factorio --create _default
VOLUME ["/opt/factorio/saves"]

CMD ["/opt/factorio/bin/x64/factorio", "--start-server", "_default"]
EXPOSE 34197/udp
