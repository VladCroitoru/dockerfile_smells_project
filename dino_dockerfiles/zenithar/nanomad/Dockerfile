FROM sdurrheimer/alpine-glibc:latest
MAINTAINER Thibault NORMAND <me@zenithar.org>

ADD entrypoint.sh .

RUN apk add --update -t build-deps wget unzip \
    && wget --no-check-certificate https://releases.hashicorp.com/nomad/0.2.3/nomad_0.2.3_linux_amd64.zip \
    && wget --no-check-certificate https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64 \
    && unzip nomad_0.2.3_linux_amd64.zip \
    && rm -f nomad_0.2.3_linux_amd64.zip \
    && mv nomad /usr/bin/nomad \
    && chmod +x /usr/bin/nomad \
    && mv gosu-amd64 /usr/bin/gosu \
    && chmod +x /usr/bin/gosu \
    && addgroup nomad \
    && adduser -s /bin/false -G nomad -S -D nomad \
    && mkdir /data \
    && chown -R nomad:nomad /data \
    && chmod a+x ./entrypoint.sh \
    && apk del --purge build-deps \
    && rm -rf /var/cache/apk/*

EXPOSE      4646 4647 4648/tcp 4648/udp
VOLUME      ["/data"]
WORKDIR     /data
ENTRYPOINT  ["/entrypoint.sh"]
CMD         ["-h"]
