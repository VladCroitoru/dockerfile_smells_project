ARG REGISTRY_VERSION=2
FROM registry:${REGISTRY_VERSION}

ARG DOCKER_REGISTRY_MANIFEST_CLEANUP_VERSION=1.0.4
ENV COMPANION_RESOURCES_DIR=/opt/docker-registry-manifest-cleanup-companion

RUN apk add --no-cache bash curl docker gettext

ADD https://raw.githubusercontent.com/mortensteenrasmussen/docker-registry-manifest-cleanup/${DOCKER_REGISTRY_MANIFEST_CLEANUP_VERSION}/docker-registry-cleanup.sh /usr/local/bin/
RUN chmod a+x /usr/local/bin/docker-registry-cleanup.sh

COPY docker-registry-manifest-cleanup-companion-entrypoint.sh /
COPY files/ ${COMPANION_RESOURCES_DIR}

ENTRYPOINT ["/docker-registry-manifest-cleanup-companion-entrypoint.sh"]
