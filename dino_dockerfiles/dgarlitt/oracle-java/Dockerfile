FROM alpine:3.2

ENV JAVA_VERSION_MAJOR=8
ENV JAVA_VERSION_MINOR=66
ENV JAVA_VERSION_BUILD=17
ENV JAVA_PACKAGE=jre
ENV JAVA_HOME=/opt/${JAVA_PACKAGE}
ENV PATH=${PATH}:${JAVA_HOME}/bin

RUN apk --update add curl ca-certificates tar && \
    curl -Ls https://circle-artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-2.21-r2.apk > /tmp/glibc-2.21-r2.apk && \
    apk add --allow-untrusted /tmp/glibc-2.21-r2.apk && \
    mkdir /opt && \
    curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" \
      http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz \
      | tar -xzf - -C /opt &&\
    ln -s /opt/${JAVA_PACKAGE}1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} ${JAVA_HOME} && \
    rm tmp/* && \
    rm -rf ${JAVA_HOME}/lib/plugin.jar \
           ${JAVA_HOME}/bin/javaws \
           ${JAVA_HOME}/lib/javaws.jar \
           ${JAVA_HOME}/lib/desktop \
           ${JAVA_HOME}/plugin \
           ${JAVA_HOME}/lib/deploy* \
           ${JAVA_HOME}/lib/*javafx* \
           ${JAVA_HOME}/lib/*jfx* \
           ${JAVA_HOME}/lib/amd64/libdecora_sse.so \
           ${JAVA_HOME}/lib/amd64/libprism_*.so \
           ${JAVA_HOME}/lib/amd64/libfxplugins.so \
           ${JAVA_HOME}/lib/amd64/libglass.so \
           ${JAVA_HOME}/lib/amd64/libgstreamer-lite.so \
           ${JAVA_HOME}/lib/amd64/libjavafx*.so \
           ${JAVA_HOME}/lib/amd64/libjfx*.so
