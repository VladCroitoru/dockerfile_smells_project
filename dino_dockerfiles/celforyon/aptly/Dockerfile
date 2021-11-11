FROM debian:buster

LABEL maintainer="Alexis Pereda <alexis@pereda.fr>"
LABEL version="2.0"
LABEL description="Debian package publisher (using aptly)"

RUN apt update \
	&& apt install --no-install-recommends --no-install-suggests -y --force-yes inotify-tools gpgv1 aptly \
	&& rm -rf /var/lib/apt/lists/*

COPY etc/aptly.conf /etc/aptly.conf
COPY bin /usr/local/bin

WORKDIR /opt/aptly

VOLUME ["/opt/aptly"]
VOLUME ["/shared"]

ENTRYPOINT ["start"]
