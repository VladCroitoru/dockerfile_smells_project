FROM httpd:2.4-alpine

MAINTAINER Andy Cobaugh <andrew.cobaugh@gmail.com>

ENV COSIGN_VERSION 3.2.0
ENV COSIGN_SHA256 6eb6ad1691c27f8f2a99611afe0ec951da626246f75b01435e615c25cde6a242
ENV COSIGN_URL http://downloads.sourceforge.net/project/cosign/cosign/cosign-${COSIGN_VERSION}/cosign-${COSIGN_VERSION}.tar.gz

RUN apk --update --no-cache add ca-certificates curl wget
RUN mkdir /build && cd /build && wget "${COSIGN_URL}" \
	&& echo "${COSIGN_SHA256}  cosign-${COSIGN_VERSION}.tar.gz" | sha256sum -c \
	&& tar -xzvf cosign-${COSIGN_VERSION}.tar.gz

# build dependencies
RUN apk --update add --virtual builddeps gcc libressl-dev musl-dev make

RUN cd /build/cosign-${COSIGN_VERSION} \
	&& ./configure --enable-apache2=/usr/local/apache2/bin/apxs || cat config.log \
	&& sed -i 's/remote_ip/client_ip/g' ./filters/apache2/mod_cosign.c \
	&& make \
	&& make install \
	&& mkdir -p /var/cosign/filter \
	&& chmod 777 /var/cosign/filter \
	&& rm -rf /build \
	&& apk del builddeps

COPY start.sh /
RUN chmod +x /start.sh
CMD /start.sh
