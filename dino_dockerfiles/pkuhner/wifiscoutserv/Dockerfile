FROM python:3-stretch

LABEL maintainer="Pierre Kuhner <pierre@pcksr.net>"

ENV GOSU_VERSION 1.10
RUN set -x \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

RUN pip install -U pip

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=wifidb.settings

RUN mkdir /app
WORKDIR /app
COPY . /app/

RUN pip install -Ur requirements.txt

RUN curl -o manuf https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=$

EXPOSE 8000

RUN chmod +x start.sh
CMD ["/app/start.sh"]
