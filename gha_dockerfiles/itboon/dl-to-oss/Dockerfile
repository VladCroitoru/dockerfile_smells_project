FROM debian:buster

#RUN echo "deb http://mirrors.aliyun.com/debian buster main" > /etc/apt/sources.list

RUN set -ex \
  ; apt-get update \
  ; apt-get install ca-certificates curl -y --no-install-recommends \
  ; rm -rf /var/lib/apt/lists/* \
  ; mkdir -p /workdir

COPY main.sh /main.sh
COPY oss-*.yml /workdir/

WORKDIR /workdir
CMD ["/bin/bash", "/main.sh"]