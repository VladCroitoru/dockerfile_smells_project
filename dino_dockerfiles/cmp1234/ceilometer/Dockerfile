FROM cmp1234/nginx-python:1.10.3-python2.7.13-alpine3.6

MAINTAINER Wang Lilong "wanglilong007@gmail.com"

ENV VERSION=6.0.0

RUN set -x \  
    && apk del python2 \
    && apk add --no-cache python2 \
    && apk add --no-cache --virtual .build-deps \
		coreutils \
		curl \
		gcc \
		linux-headers \
		make \
		musl-dev \
        libffi-dev \
        python2-dev \
        mysql-client \
	py-mysqldb \
	mariadb-dev \
		zlib \
		zlib-dev \
		libxml2-dev \
		libxml2 \
		libxslt-dev \
		libxslt \
    #&& apk add --no-cache --virtual .run-deps py-mysqldb \
    && curl -fSL https://github.com/openstack/ceilometer/archive/${VERSION}.tar.gz -o ceilometer-${VERSION}.tar.gz \
    && tar xvf ceilometer-${VERSION}.tar.gz \
    && cd ceilometer-${VERSION} \
    && pip install -r requirements.txt \
    && PBR_VERSION=${VERSION}  pip install . \
    #&& pip uninstall crypto pycrypto \
    && pip install  PyMySQL==0.7.4 pycrypto crypto \
    && cp -rf etc/* /etc/ \
    && chown 18345:18345 -R /etc/ceilometer \
    && chmod 600 -R /etc/ceilometer \
    && chmod 700 /etc/ceilometer /etc/ceilometer/rootwrap.d /etc/ceilometer/examples\
    && pip install python-openstackclient==3.12.0 \
    && cd - \
    && rm -rf ceilometer-${VERSION}* \
    && apk del .build-deps
