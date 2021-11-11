FROM maven:3.3-jdk-8-alpine

WORKDIR /build

COPY pom.xml pom.xml
COPY src/main src/main
COPY src/test src/test
COPY scripts/collect-build-info.sh collect-build-info.sh

WORKDIR /

# Docker Cloud args, from hooks/build.
ARG CACHE_TAG
ARG COMMIT_MSG
ARG DOCKER_REPO
ARG IMAGE_NAME
ARG SOURCE_BRANCH
ARG SOURCE_COMMIT
# The ARGs need to become environment variables for collect-build-info.sh
ENV CACHE_TAG     ${CACHE_TAG}
ENV COMMIT_MSG    ${COMMIT_MSG}
ENV DOCKER_REPO   ${DOCKER_REPO}
ENV IMAGE_NAME    ${IMAGE_NAME}
ENV SOURCE_BRANCH ${SOURCE_BRANCH}
ENV SOURCE_COMMIT ${SOURCE_COMMIT}

RUN cd /build \
 && mvn clean \
 && ./collect-build-info.sh \
 && mvn package \
 && rm -f target/appassembler/bin/*.bat \
 && cp -R target/appassembler/* /usr/local \
 && cd / \
 && rm -rf /build

COPY config-template.yml config.yml

EXPOSE 8080 8081

ENTRYPOINT ["/usr/local/bin/janus", "server", "config.yml"]
