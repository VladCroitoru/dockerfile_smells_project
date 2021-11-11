FROM whimsicalbees/docker-base:1.0
MAINTAINER Whimsical Bees <lena@whimsicalbees.com>

# Java Version
ENV JAVA_VERSION=8 JAVA_UPDATE=45 JAVA_BUILD=14 JAVA_PACKAGE=server-jre JAVA_HOME=/usr/lib/jvm/default-jvm

# Set environment
ENV PATH=${PATH}:${JAVA_HOME}/bin

#Install GLIBC
RUN apk --no-cache add ca-certificates
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub
RUN wget -q -O /var/cache/apk/glibc-2.23-r3.apk https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.23-r3/glibc-2.23-r3.apk
RUN wget -q -O /var/cache/apk/glibc-bin-2.23-r3.apk https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.23-r3/glibc-bin-2.23-r3.apk

# Install Glibc and Oracle server-jre 8
WORKDIR /usr/lib/jvm
RUN apk add --update libgcc && \
    apk add --allow-untrusted /var/cache/apk/glibc-2.23-r3.apk && \
    apk add --allow-untrusted /var/cache/apk/glibc-bin-2.23-r3.apk && \
    ldconfig /lib /usr/glibc/usr/lib && \
    wget --header "Cookie: oraclelicense=accept-securebackup-cookie;" \
        "http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION}u${JAVA_UPDATE}-b${JAVA_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" && \
    tar xzf "${JAVA_PACKAGE}-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" && \
    mv "jdk1.${JAVA_VERSION}.0_${JAVA_UPDATE}" java-${JAVA_VERSION}-oracle && \
    ln -s "java-${JAVA_VERSION}-oracle" $JAVA_HOME && \
    apk del libgcc && \
    rm -f ${JAVA_PACKAGE}-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz && \
    rm -f /var/cache/apk/* && \
    rm -rf default-jvm/*src.zip \
           default-jvm/lib/missioncontrol \
           default-jvm/lib/visualvm \
           default-jvm/lib/*javafx* \
           default-jvm/jre/lib/plugin.jar \
           default-jvm/jre/lib/ext/jfxrt.jar \
           default-jvm/jre/bin/javaws \
           default-jvm/jre/lib/javaws.jar \
           default-jvm/jre/lib/desktop \
           default-jvm/jre/plugin \
           default-jvm/jre/lib/deploy* \
           default-jvm/jre/lib/*javafx* \
           default-jvm/jre/lib/*jfx* \
           default-jvm/jre/lib/amd64/libdecora_sse.so \
           default-jvm/jre/lib/amd64/libprism_*.so \
           default-jvm/jre/lib/amd64/libfxplugins.so \
           default-jvm/jre/lib/amd64/libglass.so \
           default-jvm/jre/lib/amd64/libgstreamer-lite.so \
           default-jvm/jre/lib/amd64/libjavafx*.so \
           default-jvm/jre/lib/amd64/libjfx*.so