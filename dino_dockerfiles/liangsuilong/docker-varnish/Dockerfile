FROM ubuntu:16.04

MAINTAINER Suilong Liang <suilong.liang@worktogether.io>

ENV VARNISH_MAJOR 5.1
ENV VARNISH_VERSION 5.1.3
ENV VARNISH_VERSION_MINOR 1~xenial

RUN groupadd -r varnish && useradd -r -g varnish varnish

RUN set -ex; \
	\
	fetchDeps=' \
		ca-certificates \
		curl \
		gnupg \
		debian-archive-keyring \
		apt-transport-https \
	'; \
	apt-get update; \
	apt-get install -y --no-install-recommends $fetchDeps; \
	curl -L https://packagecloud.io/varnishcache/varnish51/gpgkey | apt-key add -; \
        echo "deb https://packagecloud.io/varnishcache/varnish51/ubuntu/ xenial main" >> /etc/apt/sources.list.d/varnish.list; \
	apt-get update; \
	apt-get -y install \
		varnish=${VARNISH_VERSION}-${VARNISH_VERSION_MINOR} \
		varnish-dev=${VARNISH_VERSION}-${VARNISH_VERSION_MINOR}; \
	rm -rf /var/lib/apt/lists/* 

VOLUME /var/lib/varnish/

ADD entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

EXPOSE 80
CMD ["varnish"]
