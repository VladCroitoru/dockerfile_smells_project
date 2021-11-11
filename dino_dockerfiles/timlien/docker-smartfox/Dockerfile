FROM debian

MAINTAINER Tim Lien <timlientw@gmail.com>

ENV SMARTFOX_VERSION 2_13_0
ENV SMARTFOX_PATCH_VERSION 2.13.3

RUN apt-get update && \
    apt-get install -y \
    wget \
    unzip

RUN mkdir -p /tmp

WORKDIR /tmp

RUN wget http://www.smartfoxserver.com/downloads/sfs2x/SFS2X_unix_${SMARTFOX_VERSION}.tar.gz

RUN wget http://www.smartfoxserver.com/downloads/sfs2x/patches/SFS2X-Patch-${SMARTFOX_PATCH_VERSION}.zip

WORKDIR /opt/SmartFoxServer_2X

VOLUME /opt/SmartFoxServer_2X

COPY docker-entrypoint.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/docker-entrypoint.sh && \
    ln -s /usr/local/bin/docker-entrypoint.sh /entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8080 9933 9933/udp 8787 5000

CMD ["sfs2x"]
