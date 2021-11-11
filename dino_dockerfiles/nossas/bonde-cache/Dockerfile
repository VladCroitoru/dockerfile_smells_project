FROM golang:onbuild

ARG TIMEZONE="America/Sao_Paulo"
RUN set -x \
	&& apt-get update \
	&& apt-get upgrade -y \
	&& echo "=> Needed packages:" \
    && apt-get install -y --no-install-recommends apt-utils curl ca-certificates tar openssl xz-utils \
    && echo "=> Configuring and installing timezone (${TIMEZONE}):" \
    && echo ${TIMEZONE} > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove apt-utils

VOLUME ["/go/src/app"]
WORKDIR /go/src/app
ENV CACHE_INTERVAL 30
EXPOSE 80 443
