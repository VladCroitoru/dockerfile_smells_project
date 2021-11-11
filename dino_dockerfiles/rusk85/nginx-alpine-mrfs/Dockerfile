FROM rusk85/alpine-base

ARG BUILD_TIME
ARG VERSION

LABEL	author="Sven Muncic <sven@muncic.de>" \
	description="NGINX Reverse Proxy configured with a static config to serve JIRA and Adminer on the same maschine \
			both of which are in turn also running within docker containers." \
	build-time="${BUILD_TIME}" \
	image-version="${VERSION}"

# build-time variables
ARG NGINX_RUN=/run/nginx/
ARG NGINX_INSTALL=/etc/nginx/
ARG NGINX_CONF=/etc/nginx/nginx.conf
ARG NUSER=nginx
ARG NGROUP=nginx

RUN	apk update && \
	apk add nginx && \
	mkdir -p ${NGINX_RUN} && \
	chown -R ${NUSER}:${NGROUP} ${NGINX_RUN} && \
	rm -f ${NGINX_CONF}

COPY nginx.conf ${NGINX_CONF}

EXPOSE 8080

USER root
WORKDIR ${NGINX_INSTALL}
VOLUME ["/etc/nginx/"]
CMD nginx && tail -f /dev/null
