FROM calvintam236/ubuntu:amd

MAINTAINER calvintam236 <calvintam236@users.noreply.github.com>
LABEL description="marlin in Docker. Supports GPU mining."

WORKDIR /tmp

RUN apt-get update \
    && apt-get -y --no-install-recommends install ca-certificates curl \
    && curl -L -O https://github.com/SiaMining/marlin/releases/download/v1.0.0/marlin-1.0.0-linux-amd64.tar.gz \
    && tar -xvf marlin-1.0.0-linux-amd64.tar.gz \
    && rm marlin-1.0.0-linux-amd64.tar.gz \
    && mv marlin /usr/local/bin/marlin \
    && chmod a+x /usr/local/bin/marlin \
    && apt-get -y remove ca-certificates curl \
    && apt-get -y autoremove \
    && apt-get clean autoclean \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

ENTRYPOINT ["marlin"]
CMD ["-h"]
