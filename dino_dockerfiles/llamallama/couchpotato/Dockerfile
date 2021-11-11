FROM debian:8
MAINTAINER Chris Jones

#
# Create user and group for CouchPotato.
#

RUN groupadd -r -g 10000 media \
    && useradd -r -u 10001 -G media -d /couchpotato couchpotato

#
# Install CouchPotato and all required dependencies.
#

RUN export VERSION=3.0.1 \
    && apt-get -q update \
    && apt-get install -qy curl ca-certificates python-pip python-dev libz-dev libxml2-dev libxslt1-dev gcc \
    && curl -o /tmp/couchpotato.tar.gz https://codeload.github.com/CouchPotato/CouchPotatoServer/tar.gz/build/${VERSION} \
    && tar xzf /tmp/couchpotato.tar.gz \
    && mv CouchPotatoServer-* couchpotato \
    && chown -R couchpotato: couchpotato \
    && pip install cheetah lxml pyopenssl \
    && apt-get -y remove curl python-dev libz-dev libxml2-dev libxslt1-dev gcc \
    && apt-get -y autoremove \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*

#
# Define container settings.
#
RUN mkdir -p /datadir /media \
    && chown couchpotato:media /datadir /media
    
VOLUME ["/datadir", "/media"]

EXPOSE 5050

#
# Start CouchPotato.
#

USER couchpotato
WORKDIR /couchpotato
ENTRYPOINT ["./CouchPotato.py"]
CMD ["--data_dir=/datadir"],["--config_file=$/datadir/config.ini"]
