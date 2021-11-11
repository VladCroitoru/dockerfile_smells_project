FROM buildpack-deps:jessie

RUN mkdir -p /conf

RUN apt-get update && apt-get install -y \
  libgmp-dev \
  iptables \
  xl2tpd \
  module-init-tools \
  vim \
  net-tools

ENV STRONGSWAN_VERSION 5.5.1
ENV GPG_KEY 948F158A4E76A27BF3D07532DF42C170B34DBA77

RUN mkdir -p /usr/src/strongswan \
  && mkdir -p /opt/swan/proc /opt/swan/bin /opt/swan/config  \
	&& cd /usr/src \
	&& curl -SOL "https://download.strongswan.org/strongswan-$STRONGSWAN_VERSION.tar.gz.sig" \
	&& curl -SOL "https://download.strongswan.org/strongswan-$STRONGSWAN_VERSION.tar.gz" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \
	&& gpg --batch --verify strongswan-$STRONGSWAN_VERSION.tar.gz.sig strongswan-$STRONGSWAN_VERSION.tar.gz \
	&& tar -zxf strongswan-$STRONGSWAN_VERSION.tar.gz -C /usr/src/strongswan --strip-components 1 \
	&& cd /usr/src/strongswan \
	&& ./configure --prefix=/usr --sysconfdir=/opt/swan/config --with-piddir=/opt/swan/proc --libexecdir=/opt/swan/bin \
		--enable-eap-radius \
		--enable-eap-mschapv2 \
		--enable-eap-identity \
		--enable-eap-md5 \
		--enable-eap-mschapv2 \
		--enable-eap-tls \
		--enable-eap-ttls \
		--enable-eap-peap \
		--enable-eap-tnc \
		--enable-eap-dynamic \
		--enable-xauth-eap \
		--enable-openssl \
		--enable-unity \
		--disable-ikev2 \
	&& make -j \
	&& make install \
	&& rm -rf "/usr/src/strongswan*"

ADD run.sh /run.sh
VOLUME ["/opt/swan"]

EXPOSE 4500/udp 500/udp 1701/udp
CMD ["/run.sh"]
