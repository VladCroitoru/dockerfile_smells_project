FROM debian:jessie
MAINTAINER Luca Crea <lucacrea@yahoo.it>


RUN set -ex \
    && addgroup --system --gid 500 libreoffice \
    && adduser --disabled-password --system --disabled-login --shell /sbin/nologin --gid 500 --uid 500 libreoffice


ENV GOSU_VERSION 1.10
RUN set -x \
    && apt-get update && apt-get install -y --no-install-recommends ca-certificates wget && rm -rf /var/lib/apt/lists/* \
    && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true \
    && apt-get purge -y --auto-remove ca-certificates wget


# @BUGFIX
# It's important to install the full LibreOffice suite, otherwise OpenERP will
# display this error:
#
#   - Unsupported URL <private:stream>: ""
#
RUN set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
       libreoffice \
    && rm -rf /var/lib/apt/lists/*


VOLUME ["/usr/local/share/fonts/"]

EXPOSE 8100

COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD ["soffice-headless"]
