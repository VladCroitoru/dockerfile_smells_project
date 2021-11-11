FROM dockette/alpine:edge

# Base on https://raw.githubusercontent.com/wernight/docker-compose/master/Dockerfile

ENV GLIBC_VERSION=2.28-r0
ENV DOCKER_COMPOSE_VERSION=1.23.2

RUN set -x && \
   echo '@community http://nl.alpinelinux.org/alpine/edge/community' >> /etc/apk/repositories && \
   apk update && \
   apk upgrade && \
   apk add --no-cache docker@community make git && \
   apk add --no-cache -t .deps ca-certificates wget curl && \
   wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
   wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk && \
   wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk && \
   apk add glibc-${GLIBC_VERSION}.apk glibc-bin-${GLIBC_VERSION}.apk && \
   rm glibc-${GLIBC_VERSION}.apk glibc-bin-${GLIBC_VERSION}.apk && \
   # Install docker-compose
   curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-Linux-x86_64 > /usr/local/bin/docker-compose && \
   chmod a+rx /usr/local/bin/docker-compose && \
   # Basic check it works
   docker-compose version && \
   # Clean-up
   apk del .deps

CMD ["/bin/sh"]
