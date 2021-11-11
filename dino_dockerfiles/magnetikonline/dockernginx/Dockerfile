FROM ubuntu:18.04 AS build

ARG NGINX_VERSION

RUN DEBIAN_FRONTEND="noninteractive" \
	apt-get update && \
	apt-get --no-install-recommends --yes install \
		gcc \
		libpcre3-dev \
		make \
		zlib1g-dev

ADD "https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz" /root/build/
RUN tar \
	--directory /root/build \
	--extract \
	--file "/root/build/nginx-$NGINX_VERSION.tar.gz"

WORKDIR "/root/build/nginx-$NGINX_VERSION"
ADD ./resource/configure.sh .

RUN chmod u+x configure.sh
RUN ./configure.sh && \
	make install


FROM ubuntu:18.04
LABEL maintainer="Peter Mescalchin <peter@magnetikonline.com>"

COPY --from=build /usr/local/sbin/nginx /usr/local/sbin/nginx
RUN mkdir /usr/local/nginx
VOLUME ["/etc/nginx","/srv/http","/var/log/nginx"]

EXPOSE 80/tcp 443/tcp

ENTRYPOINT ["/usr/local/sbin/nginx"]
CMD ["-g","daemon off;lock_file /run/lock/nginx.lock;"]
