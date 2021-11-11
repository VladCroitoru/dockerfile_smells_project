FROM alpine:3.12

ENV PKG_CONFIG_PATH /usr/local/lib/pkgconfig/:/usr/lib/pkgconfig/

RUN buildDeps=" \
		curl \
		g++ \
		gnutls-dev \
		gpgme \
		libev-dev \
		libnl3-dev \
		libseccomp-dev \
		linux-headers \
		linux-pam-dev \
		lz4-dev \
		make \
		readline-dev \
		tar \
		xz \
		autoconf \
		libtool \
		automake \
		abi-compliance-checker \
	"; \
	set -x \
	&& apk update \
	&& apk add gnutls gnutls-utils iptables libev libintl libnl3 libseccomp linux-pam lz4 lz4-libs openssl readline sed \
	&& apk add $buildDeps \
	&& RADCLI_VERSION=`curl "https://api.github.com/repos/radcli/radcli/releases/latest" | sed -n 's/^.*"tag_name": "\(.*\)",$/\1/p'` \
  && curl -SL "https://github.com/radcli/radcli/releases/download/$RADCLI_VERSION/radcli-$RADCLI_VERSION.tar.gz" -o radcli.tar.gz \
	&& mkdir -p /usr/src/radcli \
	&& tar -xf radcli.tar.gz -C /usr/src/radcli --strip-components=1 \
	&& rm radcli.tar.gz* \
	&& cd /usr/src/radcli \
	&& ./configure --sysconfdir=/etc/ \
	&& make \
	&& make install \
	&& cd / \
	&& rm -fr /usr/src/radcli \
	&& OC_VERSION=`curl "http://ocserv.gitlab.io/www/download.html" | sed -n 's/^.*version is <b>\(.*$\)/\1/p'` \
	&& curl -SL "ftp://ftp.infradead.org/pub/ocserv/ocserv-$OC_VERSION.tar.xz" -o ocserv.tar.xz \
	&& curl -SL "ftp://ftp.infradead.org/pub/ocserv/ocserv-$OC_VERSION.tar.xz.sig" -o ocserv.tar.xz.sig \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-key 96865171 \
	&& gpg --verify ocserv.tar.xz.sig \
	&& mkdir -p /usr/src/ocserv \
	&& tar -xf ocserv.tar.xz -C /usr/src/ocserv --strip-components=1 \
	&& rm ocserv.tar.xz* \
	&& cd /usr/src/ocserv \
	&& ./configure \
	&& make \
	&& make install \
	&& mkdir -p /etc/ocserv \
	&& cp /usr/src/ocserv/doc/sample.config /etc/ocserv/ocserv.conf \
	&& cd / \
	&& rm -fr /usr/src/ocserv \
	&& apk del $buildDeps \
	&& rm -rf /var/cache/apk/*

# Setup config
COPY groupinfo.txt /tmp/
RUN set -x \
	&& sed -i 's/\.\/sample\.passwd/\/etc\/ocserv\/ocpasswd/' /etc/ocserv/ocserv.conf \
	&& sed -i 's/\(max-same-clients = \)2/\110/' /etc/ocserv/ocserv.conf \
	&& sed -i 's/^max-clients = 16/max-clients = 512/' /etc/ocserv/ocserv.conf \
	&& sed -i 's/\.\.\/tests/\/etc\/ocserv/' /etc/ocserv/ocserv.conf \
	&& sed -i 's/#\(compression.*\)/\1/' /etc/ocserv/ocserv.conf \
	&& sed -i '/^ipv4-network = /{s/192.168.1.0/10.205.0.0/}' /etc/ocserv/ocserv.conf \
	&& sed -i '/^ipv4-netmask = /{s/255.255.255.0/255.255.0.0/}' /etc/ocserv/ocserv.conf \
	&& sed -i 's/^dns = 192.168.1.2/dns = 208.67.222.222\ndns = 8.8.8.8/' /etc/ocserv/ocserv.conf \
	&& sed -i 's/^route/#route/' /etc/ocserv/ocserv.conf \
	&& sed -i 's/^no-route/#no-route/' /etc/ocserv/ocserv.conf \
  && mkdir -p /etc/ocserv/config-per-group \
	&& cat /tmp/groupinfo.txt >> /etc/ocserv/ocserv.conf \
	&& rm -fr /tmp/cn-no-route.txt \
  && rm -fr /tmp/groupinfo.txt

WORKDIR /etc/ocserv

COPY All /etc/ocserv/config-per-group/All
COPY cn-no-route.txt /etc/ocserv/config-per-group/Route
COPY Local /etc/ocserv/config-per-group/Local

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 443
CMD ["ocserv", "-c", "/etc/ocserv/ocserv.conf", "-f"]
