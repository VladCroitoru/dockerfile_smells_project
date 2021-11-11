FROM docker:latest

# Java Version
ENV JAVA_VERSION=8 JAVA_UPDATE=91 JAVA_BUILD=14 JAVA_PACKAGE=server-jre JAVA_HOME=/usr/lib/jvm/default-jvm

# SBT environment
ENV SBT_VERSION=0.13.13 SBT_HOME=/usr/local/sbt
ENV SBT_OPTS -Xms1G -Xmx2G -Xss1M -XX:+CMSClassUnloadingEnabled -XX:MaxPermSize=1G

# Set environment
ENV PATH=${PATH}:${JAVA_HOME}/bin
ENV PATH=${PATH}:${SBT_HOME}/bin

# Copy apks
COPY /lib /var/cache/apk

# Install Glibc and Oracle server-jre 8
WORKDIR /usr/lib/jvm

RUN apk update && apk upgrade && \
    apk add --update openssh-client && \
    apk add --update bash wget curl tree git bc && \
    apk add --update libgcc && \
    apk add --allow-untrusted /var/cache/apk/glibc-2.21-r2.apk && \
    apk add --allow-untrusted /var/cache/apk/glibc-bin-2.21-r2.apk && \
    /usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib && \
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
           default-jvm/jre/lib/amd64/libjfx*.so && \
    echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf && \
    echo -ne "- with `java -version 2>&1 | awk 'NR == 2'`\n" >> /root/.built

# Install sbt
RUN mkdir -p $SBT_HOME && \
    curl -sL "http://dl.bintray.com/sbt/native-packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C $SBT_HOME --strip-components=1

WORKDIR /app
