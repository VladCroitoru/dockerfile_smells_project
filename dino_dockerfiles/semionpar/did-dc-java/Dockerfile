FROM docker

ENV LANG C.UTF-8

ENV JAVA_HOME="/jdk-12"
ARG JDK_BUILD="14"
ENV JDK_ARCHIVE="openjdk-12-ea+${JDK_BUILD}_linux-x64-musl_bin.tar.gz"

RUN wget https://download.java.net/java/early_access/alpine/${JDK_BUILD}/binaries/${JDK_ARCHIVE}
RUN wget https://download.java.net/java/early_access/alpine/${JDK_BUILD}/binaries/${JDK_ARCHIVE}.sha256
RUN echo "  ${JDK_ARCHIVE}" >> ${JDK_ARCHIVE}.sha256
RUN sha256sum -c ${JDK_ARCHIVE}.sha256
RUN tar -xzf ${JDK_ARCHIVE}
RUN rm ${JDK_ARCHIVE} ${JDK_ARCHIVE}.sha256
RUN rm ${JAVA_HOME}/lib/src.zip

ENV PATH=$PATH:${JAVA_HOME}/bin

ENV JAVA_VERSION 12-ea+${JDK_BUILD}
ENV JAVA_ALPINE_VERSION 12~${JDK_BUILD}-1

RUN echo $PATH

RUN set -x \
    && apk add --no-cache py-pip bash openssh git

RUN set -x \
    && pip install --no-cache-dir docker-compose \
    && docker-compose -v
