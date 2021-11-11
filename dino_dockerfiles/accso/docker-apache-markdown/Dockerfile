FROM httpd:2.4.25-alpine
MAINTAINER marcus.rickert@accso.de

ENV DISCOUNT_DIR=/tmp/discount
ARG DISCOUNT_VERSION=2.2.2
ENV DISCOUNT_PACKAGE=http://www.pell.portland.or.us/~orc/Code/discount/discount-${DISCOUNT_VERSION}.tar.bz2
ENV DISCOUNT_INSTALL_DIR=/usr/local

ENV MARKDOWN_DIR=/tmp/apache-mod-markdown
ARG MARKDOWN_VERSION=1.0.3
ENV MARKDOWN_PACKAGE=https://github.com/hamano/apache-mod-markdown/archive/${MARKDOWN_VERSION}.zip

# See https://bbs.archlinux.org/viewtopic.php?id=161452

RUN set -x \
	&& apk add --no-cache --virtual .build-deps \
		ca-certificates \
		openssl \
		gcc \
		gnupg \
		libc-dev \
		libtool \
		make \
		autoconf \
		automake \
		tar \
		bash \
	&& mkdir -p ${DISCOUNT_DIR} \
	&& cd ${DISCOUNT_DIR} \
	&& echo "Downloading ${DISCOUNT_PACKAGE}..." \
	&& wget -nv ${DISCOUNT_PACKAGE} \
	&& bunzip2 discount-${DISCOUNT_VERSION}.tar.bz2 \
	&& tar xf discount-${DISCOUNT_VERSION}.tar \
	&& cd discount-${DISCOUNT_VERSION} \
	&& echo "Building discount..." \
	&& CFLAGS="-O2 -g -fPIC" ./configure.sh \
	&& make \
	&& make install \
	&& mkdir -p ${MARKDOWN_DIR} \
	&& cd ${MARKDOWN_DIR} \
	&& echo "Downloading ${MARKDOWN_PACKAGE}..." \
	&& wget -nv ${MARKDOWN_PACKAGE} -O markdown.zip \
	&& unzip markdown.zip \
	&& cd apache-mod-markdown-${MARKDOWN_VERSION} \
	&& echo "Building apache-mod-markdown..." \	
	&& libtoolize --force \
        && aclocal \
        && autoheader \
        && automake --force-missing --add-missing \
        && autoreconf  -f -i \
        && ./configure --with-apxs=/usr/local/apache2/bin/apxs --with-discount=${DISCOUNT_INSTALL_DIR} \
        && make \
        && make install \
	&& cd / \
	&& echo "Cleaning up..." \
	&& rm -rf ${DISCOUNT_DIR} \
	&& rm -rf ${MARKDOWN_DIR}
