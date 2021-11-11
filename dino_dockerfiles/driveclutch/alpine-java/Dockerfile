#
# Base layer for apps using a JVM
#
# This image will contain an Official Oracle version of Java.
#
# Parts of the JRE not required for running server apps are
#   removed to save space.
#
#
FROM alpine:3.3
MAINTAINER David Hallum <david@driveclutch.com>

# The variables below control what style and version of
#   Oracle Java is install
#
# JDL_TYPE can be jdk, jre, or server-jre
#
ENV JDL_TYPE "server-jre"
ENV JDL_VERSION "8"
ENV JDL_UPDATE "92"
ENV JDL_BUILD "14"
ENV OPENSSL_VER "1.0.2g"
ENV GLIBC_VERSION "2.23-r1"

###################################################
#  Use caution adjusting anything below this line #
#    A small change can have a great impact       #
###################################################

#
# Download and Install Oracle Java
#
# Java SE JDK http://download.oracle.com/otn/java/jdk/7u80-b15/jdk-7u80-linux-i586.tar.gz
# Java SE JRE http://download.oracle.com/otn/java/jdk/7u80-b15/jre-7u80-linux-i586.tar.gz
# Server SE JRE http://download.oracle.com/otn-pub/java/jdk/8u92-b14/server-jre-8u92-linux-x64.tar.gz
#

ENV JAVA_HOME "/usr/lib/jvm/java-${JDL_VERSION}-oracle"

# Download and install Oracle JAVA and OpenSSL
RUN apk --update add \
      bash \
      curl \
      ca-certificates \
      perl \
      alpine-sdk && \
    curl -Ls https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk > /tmp/glibc-${GLIBC_VERSION}.apk && \
    apk add --allow-untrusted /tmp/glibc-${GLIBC_VERSION}.apk && \
    curl -Ls https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk > /tmp/glibc-bin-${GLIBC_VERSION}.apk && \
    apk add --allow-untrusted /tmp/glibc-bin-${GLIBC_VERSION}.apk && \
    /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc/usr/lib && \
    curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o /tmp/java.tar.gz \
         http://download.oracle.com/otn-pub/java/jdk/"${JDL_VERSION}"u"${JDL_UPDATE}"-b"${JDL_BUILD}"/jdk-"${JDL_VERSION}"u"${JDL_UPDATE}"-linux-x64.tar.gz && \
    gunzip /tmp/java.tar.gz && \
    tar x -C /tmp/ -f /tmp/java.tar && \
    mkdir -p /usr/lib/jvm && \
    mv /tmp/jdk1.${JDL_VERSION}.0_${JDL_UPDATE} "${JAVA_HOME}" && \
    curl -jksSL https://www.openssl.org/source/openssl-${OPENSSL_VER}.tar.gz \
      | gunzip -c \
      | tar x -C /tmp && \
    cd /tmp/openssl-${OPENSSL_VER} && \
      ./config --prefix=/usr && \
      make depend && \
      make && \
      make install && \
    # Clean-up and slim down the installed files
    find ${JAVA_HOME} -maxdepth 1 -mindepth 1 | egrep -v 'jre|bin' | xargs rm -rf && \
    apk del curl alpine-sdk perl && \
    rm -rf \
      ${JAVA_HOME}/jre/plugin \
      ${JAVA_HOME}/jre/bin/javaws \
      ${JAVA_HOME}/jre/bin/jjs \
      ${JAVA_HOME}/jre/bin/keytool \
      ${JAVA_HOME}/jre/bin/orbd \
      ${JAVA_HOME}/jre/bin/pack200 \
      ${JAVA_HOME}/jre/bin/policytool \
      ${JAVA_HOME}/jre/bin/rmid \
      ${JAVA_HOME}/jre/bin/rmiregistry \
      ${JAVA_HOME}/jre/bin/servertool \
      ${JAVA_HOME}/jre/bin/tnameserv \
      ${JAVA_HOME}/jre/bin/unpack200 \
      ${JAVA_HOME}/bin/javaws \
      ${JAVA_HOME}/bin/jjs \
      ${JAVA_HOME}/bin/keytool \
      ${JAVA_HOME}/bin/orbd \
      ${JAVA_HOME}/bin/pack200 \
      ${JAVA_HOME}/bin/policytool \
      ${JAVA_HOME}/bin/rmid \
      ${JAVA_HOME}/bin/rmiregistry \
      ${JAVA_HOME}/bin/servertool \
      ${JAVA_HOME}/bin/tnameserv \
      ${JAVA_HOME}/bin/unpack200 \
      ${JAVA_HOME}/jre/lib/javaws.jar \
      ${JAVA_HOME}/jre/lib/deploy* \
      ${JAVA_HOME}/jre/lib/desktop \
      ${JAVA_HOME}/jre/lib/*javafx* \
      ${JAVA_HOME}/jre/lib/*jfx* \
      ${JAVA_HOME}/jre/lib/amd64/libdecora_sse.so \
      ${JAVA_HOME}/jre/lib/amd64/libprism_*.so \
      ${JAVA_HOME}/jre/lib/amd64/libfxplugins.so \
      ${JAVA_HOME}/jre/lib/amd64/libglass.so \
      ${JAVA_HOME}/jre/lib/amd64/libgstreamer-lite.so \
      ${JAVA_HOME}/jre/lib/amd64/libjavafx*.so \
      ${JAVA_HOME}/jre/lib/amd64/libjfx*.so \
      ${JAVA_HOME}/jre/lib/ext/jfxrt.jar \
      ${JAVA_HOME}/jre/lib/ext/nashorn.jar \
      ${JAVA_HOME}/jre/lib/oblique-fonts \
      ${JAVA_HOME}/jre/lib/plugin.jar \
      /var/cache/apk/* \
      /tmp/* && \
    # Update the JVM ttl to 0s (NO internal caching! respect the DNS TTL settings)
    grep -v 'networkaddress.cache.ttl' $JAVA_HOME/jre/lib/security/java.security | grep -v 'networkaddress.cache.negative.ttl' > $JAVA_HOME/jre/lib/security/java.security.tmp && \
    echo 'networkaddress.cache.ttl=0' >> $JAVA_HOME/jre/lib/security/java.security.tmp && \
    echo 'networkaddress.cache.negative.ttl=0' >> $JAVA_HOME/jre/lib/security/java.security.tmp && \
    mv $JAVA_HOME/jre/lib/security/java.security.tmp $JAVA_HOME/jre/lib/security/java.security && \
    # App Service User
    mkdir /app && \
    addgroup app && \
    adduser -G app -s /sbin/nologin -g "App Service Account" -h /app -D app && \
    chown -R app:app /app

ENV LD_LIBRARY_PATH="${JAVA_HOME}/jre/lib/amd64/jli"
ENV PATH="${JAVA_HOME}/bin:$PATH"

USER app
WORKDIR /app
