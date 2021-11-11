FROM fizzka/php-embed:7.4.5-alpine

ARG UNIT_VERSION=1.17.0
ARG CONTROL=0.0.0.0:8400

RUN set -eux -o pipefail; \
	export UNIT_URL=https://unit.nginx.org/download/unit-${UNIT_VERSION}.tar.gz; \
	\
	wget -q "${UNIT_URL}"; \
	wget -qO- "${UNIT_URL}.sha512" | sha512sum -c; \
	tar xf unit-${UNIT_VERSION}.tar.gz; \
	\
	apk add --no-cache --virtual .build-deps $PHPIZE_DEPS; \
	\
	( \
		cd unit-${UNIT_VERSION}; \
		./configure \
			--control=${CONTROL} \
			--log=/dev/fd/2 \
			--state=/var/lib/unit \
			--pid=/run/unit.pid \
			--tmp=/tmp \
			--prefix=/usr/local; \
		./configure php --module=php74; \
		make; \
		make install \
	); \
	\
	rm -rf unit*; \
	\
	apk del --no-network .build-deps

EXPOSE 8400

CMD ["unitd", "--no-daemon"]
