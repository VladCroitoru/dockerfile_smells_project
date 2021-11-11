FROM cmp1234/nginx-python:1.10.3-python2.7.13-alpine3.6

MAINTAINER Wang Lilong "wanglilong007@gmail.com"

ENV VERSION=10.0.0.0b1

RUN set -x \  
    && apk add --no-cache --virtual .build-deps \
		coreutils \
		curl \
		gcc \
		linux-headers \
		make \
		musl-dev \
		zlib \
		libffi-dev \
                python-dev \
		zlib-dev \
		mariadb-dev \
    && curl -fSL https://github.com/openstack/keystone/archive/${VERSION}.tar.gz -o keystone-${VERSION}.tar.gz \
    && tar xvf keystone-${VERSION}.tar.gz \
    && cd keystone-${VERSION} \
    && pip install -r requirements.txt \
    && PBR_VERSION=${VERSION}  pip install . \
    && pip install uwsgi==2.0.15 PyMySQL==0.7.4 \
    && apk add --no-cache --virtual .run-deps  \
    	libffi=3.2.1-r3 \
    #    mysql-client \
	#py-mysqldb \
    && cp -r etc /etc/keystone \
    && pip install python-openstackclient==3.12.0 \
    && cd - \
    && rm -rf keystone-${VERSION}* \
    && apk del .build-deps
