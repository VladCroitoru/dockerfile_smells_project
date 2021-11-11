FROM alpine:latest
# australian timezone
RUN apk add tzdata --no-cache \
&&  cp /usr/share/zoneinfo/Australia/Hobart /etc/localtime \
&&  apk del -r tzdata

# s6-overlay
ENV S6_VERSION v1.18.1.5
ENV S6_URL https://github.com/just-containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz

# download & extract to root
RUN apk add --no-cache curl openssl \
&&  curl -sSL ${S6_URL} | tar -C / -xzf -


ENV DOCKER_VERSION 17.06.2-ce
ENV DOCKER_DOWNLOAD_URL "https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz"
ENV DOCKER_GC_URL=https://raw.githubusercontent.com/spotify/docker-gc/bb9580df7205da8498f41a5be05aeaeeff012f54/docker-gc

RUN echo ${DOCKER_DOWNLOAD_URL} > /dev/stderr

WORKDIR /tmp
RUN apk add --no-cache openssl curl bash \
&&  curl -L ${DOCKER_DOWNLOAD_URL} | tar zxf - \
&&  mkdir -p /usr/local/bin/ \
&&  mv "$(find -type f -name 'docker')" /usr/local/bin/ \
&&  chmod +x /usr/local/bin/docker \
&&  wget ${DOCKER_GC_URL} -O /usr/sbin/docker-gc \
&&  chmod +x /usr/sbin/docker-gc \
&&  chown root:root /usr/sbin/docker-gc

# remove unused packages & data
RUN apk del curl openssl \
&&  rm -rf /tmp/* \
&&  rm -rf /var/cache/apk/*



# run docker-gc hourly
ADD include/docker-gc-run /etc/periodic/hourly/
# start crond
ADD include/run_crond /etc/services.d/crond/run

RUN chmod +x /etc/periodic/hourly/docker-gc-run
# s6-overlay entry
ENTRYPOINT ["/init"]
# simple crond start
CMD []


