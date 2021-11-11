FROM alpine:latest AS builder
LABEL Description="Finance Build Container for aqbanking"

# install prerequisited
RUN \
	set -x && \
	apk add \
		autoconf \
		automake \
		bash \
		build-base \
		bzip2 \
		curl \
		gettext-dev \
		glib-dev \
		git \
		gmp-dev \
		gnutls-dev \
		intltool \
		libffi-dev \
		libgcrypt-dev \
		libtool \
		libxslt-dev \
		libxml2-dev \
		mysql-dev \
		xmlsec-dev
	#----- end for alpine

# gwenhywfar
RUN \
	set -x && \
	git clone https://github.com/aqbanking/gwenhywfar && \
	cd gwenhywfar && \
	git checkout tags/5.7.3 && \
	sed -i 's:i18n_libs="$LIBS":i18n_libs="$LIBS -lintl":' configure.ac && \
	make -f Makefile.cvs && \
	./configure \
		--with-guis="cpp" \
		--enable-error-on-warning \
		--disable-network-checks && \
	make && \
	make install && \
	make DESTDIR=$PWD/dist install

# aqbanking
RUN \
	set -x && \
	git clone https://github.com/aqbanking/aqbanking && \
	cd aqbanking && \
	git checkout tags/6.3.2 && \
	sed -i 's:i18n_libs="$LIBS":i18n_libs="$LIBS -lintl":' configure.ac && \
	ACLOCAL_FLAGS="-I /usr/local/share/aclocal" make -f Makefile.cvs && \
	./configure && \
	make typedefs && \
	make typefiles && \
	make && \
	make install && \
	make DESTDIR=$PWD/dist install

# pxlib, a paradox DB library
RUN \
	set -x && \
	curl -L http://downloads.sourceforge.net/sourceforge/pxlib/pxlib-0.6.8.tar.gz | tar xvz && \
	cd pxlib-0.6.8 && \
	touch config.rpath && \
	autoreconf && \
	./configure \
		--prefix=/usr/local \
		--with-gsf \
		--disable-static && \
	make && \
	make install && \
	make DESTDIR=$PWD/dist install

# fntxt2sql
RUN \
	mkdir /fntxt2sql
COPY fntxt2sql/* /fntxt2sql/
RUN \
	set -x && \
	cd fntxt2sql && \
	make clean && \
	make && \
	mkdir -p dist/usr/local/bin && \
	cp -a fntxt2sql  dist/usr/local/bin/

##############################################################################
FROM alpine:edge

LABEL org.opencontainers.image.authors="Stefan Schallenberg aka nafets227 <infos@nafets.de>"
LABEL Description="Finance Container"

VOLUME /finance

ARG DEBUG=0
RUN \
	set -x && \
	apk add --no-cache --update \
		bash \
		ca-certificates \
		findutils \
		gettext \
		grep \
		iputils \
		mariadb-client \
		mariadb-connector-c \
		s-nail \
		xmlsec \
		gmp \
		gnutls \
		&& \
	if [ "$DEBUG" == "1" ] ; then \
		echo deleting files not needed: && \
		find \
			/var/cache/apk \
			/usr/share/man \
			/tmp \
			/var/tmp \
			-type f \
		; \
	fi && \
	rm -rf \
		/var/cache/apk/* \
		/usr/share/man/* \
		/tmp/* \
		/var/tmp/*

COPY --from=builder /gwenhywfar/dist/usr/local /usr/local
COPY --from=builder /aqbanking/dist /
COPY --from=builder /pxlib-0.6.8/dist /
COPY --from=builder /fntxt2sql/dist /

# copy and install additional scripts
COPY finance-root-wrapper finance-entrypoint /usr/local/bin/

RUN \
	set -x && \
	adduser -D -h /finance finance finance && \
	chown root:root /usr/local/bin/* && \
	chmod 755 /usr/local/bin/*

ENTRYPOINT [ "/usr/local/bin/finance-root-wrapper" ]
