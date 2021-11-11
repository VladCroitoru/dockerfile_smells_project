FROM openjdk:8u131-jdk-alpine

RUN apk add --update bash git ca-certificates openssl
ENV HALYARD_VERSION=0.34.0
RUN git clone --branch version-$HALYARD_VERSION https://github.com/spinnaker/halyard.git /build
RUN cd /build && ./gradlew halyard-web:installDist -x test -Prelease.version=$HALYARD_VERSION

FROM openjdk:8u131-jre-alpine
COPY --from=0 /build/halyard-web/build/install /usr/local/share
RUN apk add --update bash ca-certificates; \
    rm -rf /var/cache/apk/*; \
    ln -s /usr/local/share/halyard/bin/hal /usr/local/bin/; \
    ln -s /usr/local/share/halyard/bin/halyard /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/halyard"]
