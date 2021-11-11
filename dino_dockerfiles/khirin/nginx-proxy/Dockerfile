FROM khirin/alpine

ARG     UID="2000"
ARG     GID="2000"
ARG     PORT="10080 10443"

LABEL 	maintainer="khirin" \
	name="Nginx Reverse Proxy Image" \
        nginx_version="1.10.3" \
	date="20170315" \
        image_version="1.6" \
	user="nginx" \
	uid=${UID} \
	group="nginx" \
	gid=${GID}

COPY ["sources/init.sh", "/tmp/init.sh"]

RUN	addgroup -g ${GID} nginx \
	&& adduser -D -G nginx -g "Nginx User" -s /bin/sh -u ${UID} nginx \
	&& apk --update add nginx \
	&& rm -rf /var/cache/apk/* \
	&& mkdir -p /conf /scripts \
	&& /tmp/init.sh

VOLUME ["/conf", "/scripts"]

EXPOSE ${PORT}

USER nginx

ENTRYPOINT ["/scripts/start.sh"]
