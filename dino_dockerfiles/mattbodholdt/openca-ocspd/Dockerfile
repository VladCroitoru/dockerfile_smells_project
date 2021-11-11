FROM ubuntu:bionic

RUN apt update && \
	apt install -y \
		git \
		net-tools \
		curl \
		gcc \
		make \
		libicu-dev \
		libldap-dev \
		libxml2-dev \
		libssl-dev && \
	  apt clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN git clone https://github.com/openca/libpki.git -b master --depth 1 libpki && \
	cd /libpki && \
	./configure && \
	make && \
	make install && \
	ln -s /usr/lib64/libpki.so.91 /usr/lib/libpki.so.91 && \
	cd / && \
	rm -rf /libpki

RUN git clone https://github.com/mattbodholdt/openca-ocspd-1.git -b master --depth 1 openca-ocspd && \
	cd /openca-ocspd && \
	./configure --prefix=/usr/local/ocspd && \
  make && \
  make install && \
  cd / && \
	rm -rf /usr/local/ocspd/etc/ocspd/pki/token.d/* && \
	rm -rf /usr/local/ocspd/etc/ocspd/ca.d/* && \
	rm -rf /usr/local/ocspd/etc/ocspd/ocspd.xml && \
	rm -rf /openca-ocspd

COPY ca.xml /usr/local/ocspd/etc/ocspd/ca.d/ca.xml
COPY ocspd.xml /usr/local/ocspd/etc/ocspd/ocspd.xml
COPY token.xml /usr/local/ocspd/etc/ocspd/pki/token.d/token.xml
COPY test_ocspd.sh /usr/local/ocspd/test_ocspd.sh

RUN useradd ocspd && \
    chown -R ocspd:ocspd /usr/local/ocspd/

ENTRYPOINT [ "/usr/local/ocspd/sbin/ocspd", "-stdout", "-c", "/usr/local/ocspd/etc/ocspd/ocspd.xml" ]
