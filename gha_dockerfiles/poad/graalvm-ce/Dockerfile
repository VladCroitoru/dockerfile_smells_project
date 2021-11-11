ARG VERSION="21.3.0"
ARG TARGET_JAVA_VERSION="11"

FROM buildpack-deps:curl as downloader

ARG VERSION
ARG TARGET_JAVA_VERSION

WORKDIR /tmp

RUN curl -sSLO https://github.com/graalvm/graalvm-ce-builds/releases/download/vm-${VERSION}/graalvm-ce-java${TARGET_JAVA_VERSION}-linux-amd64-${VERSION}.tar.gz \
 && tar xf graalvm-ce-java${TARGET_JAVA_VERSION}-linux-amd64-${VERSION}.tar.gz

FROM buildpack-deps:stable AS default

ARG VERSION
ARG TARGET_JAVA_VERSION

COPY --from=downloader /tmp/graalvm-ce-java${TARGET_JAVA_VERSION}-${VERSION} /usr/lib/jvm/graalvm-ce

ENV PATH /usr/lib/jvm/graalvm-ce/bin:${PATH}

RUN groupadd -g 1000 java \
 && useradd -g 1000 -l -m -s /bin/false -u 1000 java

USER java

FROM default AS with-native-image

USER root

RUN gu install native-image

USER java
