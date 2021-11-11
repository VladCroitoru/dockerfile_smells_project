FROM alpine:3.5

RUN apk add --no-cache --virtual .persistent-deps \
	ca-certificates \
	curl \
	libstdc++ \
	libgcc \
    openssl \
	musl \
	libressl2.5-libcrypto \
	libressl2.5-libssl

COPY biosocks2.cpp /usr/src/

# Prepare build
RUN set -xe \
	&& apk add --no-cache --virtual .build-deps \
		g++ \
		gcc \
		libc-dev \
	&& mkdir -p /usr/src \
	&& cd /usr/src \
	&& g++ -o /usr/local/bin/biosocks2 biosocks2.cpp \
	&& chmod +x /usr/local/bin/biosocks2 \
	&& apk del .build-deps

EXPOSE 8080

CMD ["biosocks2", "-f"]
