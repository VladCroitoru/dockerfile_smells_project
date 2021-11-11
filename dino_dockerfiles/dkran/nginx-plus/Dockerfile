# nginx dockerfile to expose volumes for certs, the main config (nginx.conf),
# and including all of a sites-available folder for virtual hosts.  This will suit my needs

FROM nginx

MAINTAINER Daryl Kranec <dkranec@gmail.com>

ENV GOSU_VERSION 1.7
RUN set -x \
	&& apt-get update && apt-get install -y --no-install-recommends ca-certificates wget && rm -rf /var/lib/apt/lists/* \
	&& wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
	&& wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
	&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu \
	&& gosu nobody true \
	&& apt-get purge -y --auto-remove ca-certificates wget

RUN ["usermod", "--uid", "1010", "nginx"]

RUN ["groupmod", "--gid", "1010", "nginx"]

RUN ["rm","-rf","/etc/nginx/conf.d"]

RUN ["mkdir", "/usr/share/nginx-bootstrap"]

RUN ["chown","-R","1010:1010","/etc/nginx","/var/log/nginx","/srv/http","/usr/share/nginx-bootstrap"]

COPY data/etc-nginx.tar.gz /usr/share/nginx-bootstrap/

COPY data/http.tar.gz /usr/share/nginx-bootstrap/

COPY data/new-flag /usr/share/nginx-bootstrap/

COPY data/entrypoint.sh /

RUN ["chmod","775","/entrypoint.sh"]

RUN ["rm","-rf","/usr/share/nginx"]

VOLUME ["/srv/http","/etc/nginx/","/var/log/nginx/"]

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 80
EXPOSE 443
