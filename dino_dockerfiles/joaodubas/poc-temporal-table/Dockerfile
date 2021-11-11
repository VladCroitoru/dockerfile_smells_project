FROM python:3.10.0
LABEL maintainer="Joao Paulo Dubas <joao.dubas@gmail.com>" \
    version="1.0" \
    description="POC using django and temporal tables to handle accounting app."

# set user/group
RUN groupadd -r account --gid 1000 \
    && useradd -r -g account --uid=1000 account

# grab gosu for easy step-down from root
ENV GOSU_VERSION 1.10
ENV GOSU_URL "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION"
RUN set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        wget \
    && rm -rf /var/lib/apt/lists/* \
    && wget -O \
        /usr/local/bin/gosu \
        "$GOSU_URL/gosu-$(dpkg --print-architecture)" \
    && wget -O \
        /usr/local/bin/gosu.asc \
        "$GOSU_URL/gosu-$(dpkg --print-architecture).asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true \
    && apt-get purge -y --auto-remove ca-certificates wget

# make the "en_US.UTF-8" locale
RUN apt-get update \
    && apt-get install -y locales \
    && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

# entrypoint for container
COPY ./docker-entrypoint.sh /usr/local/bin
ENTRYPOINT ["docker-entrypoint.sh"]

# volume and command executed
VOLUME /opt/src
WORKDIR /opt/src
CMD ["python"]

# install system deps
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
