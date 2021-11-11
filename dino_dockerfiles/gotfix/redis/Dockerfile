FROM redis:3-alpine
MAINTAINER ian@phpb.com


ARG BUILD_DATE
ARG VCS_REF
ARG VCS_BRANCH
ARG VERSION

LABEL org.label-schema.schema-version="1.0" \
      org.label-schema.name="Docker Redis" \
      org.label-schema.description="Dockerized Redis for use with Gitlab CE" \
      org.label-schema.usage="https://gotfix.com/docker/redis/blob/master/README.md" \
      org.label-schema.url="https://gotfix.com/docker/redis" \
      org.label-schema.vcs-url=https://gotfix.com/docker/redis.git \
      org.label-schema.vendor="Ian Matyssik <ian@phpb.com>" \
      org.label-schema.vcs-ref="${VCS_REF}" \
      org.label-schema.version="${VERSION}" \
      org.label-schema.build-date="${BUILD_DATE}" \
      com.gotfix.maintainer="ian@phpb.com" \
      com.gotfix.license=MIT \
      com.gotfix.docker.dockerfile="/Dockerfile"

ENV REDIS_USER=redis \
    REDIS_DATA_DIR=/var/lib/redis \
    REDIS_LOG_DIR=/var/log/redis

COPY entrypoint.sh /usr/local/bin/docker-entrypoint.sh
COPY redis.conf /etc/redis.conf
RUN chmod 755 /usr/local/bin/docker-entrypoint.sh

EXPOSE 6379/tcp
VOLUME ["${REDIS_DATA_DIR}", "${REDIS_LOG_DIR}"]
WORKDIR ${REDIS_DATA_DIR}
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
