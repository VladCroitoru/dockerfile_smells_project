FROM certbot/certbot:latest

ENV DOCKER_CHANNEL stable
ENV DOCKER_VERSION 17.12.0-ce

RUN set -ex; \
    apk add --no-cache --virtual .fetch-deps \
    		curl \
    		tar; \
    apkArch="$(apk --print-arch)"; \
    case "$apkArch" in \
      		x86_64) dockerArch='x86_64' ;; \
      		aarch64) dockerArch='aarch64' ;; \
      		ppc64le) dockerArch='ppc64le' ;; \
      		s390x) dockerArch='s390x' ;; \
      		*) echo >&2 "error: unsupported architecture ($apkArch)"; exit 1 ;;\
      	esac; \
      	\
      	if ! curl -fL -o docker.tgz "https://download.docker.com/linux/static/${DOCKER_CHANNEL}/${dockerArch}/docker-${DOCKER_VERSION}.tgz"; then \
      		echo >&2 "error: failed to download 'docker-${DOCKER_VERSION}' from '${DOCKER_CHANNEL}' for '${dockerArch}'"; \
      		exit 1; \
      	fi; \
      	\
    tar xvf docker.tgz;\
    cp docker/docker /usr/local/bin/; \
    rm -rf docker.tgz docker; \
	apk del .fetch-deps; \
	docker -v


ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Certbot with Docker" \
      org.label-schema.description="Certbot image with Docker added to it" \
      org.label-schema.url="https://hub.docker.com/r/mumblepins/certbot-with-docker" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/mumblepins/certbot-with-docker.git" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0" \
      maintainer="Daniel Sullivan <https://github.com/mumblepins>"

CMD ["/bin/sh"]
