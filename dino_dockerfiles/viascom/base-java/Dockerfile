FROM alpine:3.7

LABEL maintainer="technical@viascom.ch"

ENV JAVA_HOME=/opt/jdk
ENV PATH=${PATH}:/opt/jdk/bin
ENV GLIBC_REPO=https://github.com/sgerrand/alpine-pkg-glibc
ENV GLIBC_VERSION=2.27-r0
ENV LANG en_US.UTF-8

RUN set -ex && \
    apk upgrade --update && \
    apk add --update libstdc++ curl ca-certificates bash java-cacerts && \
    for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION} glibc-i18n-${GLIBC_VERSION}; do curl -sSL ${GLIBC_REPO}/releases/download/${GLIBC_VERSION}/${pkg}.apk -o /tmp/${pkg}.apk; done && \
    apk add --allow-untrusted /tmp/*.apk && \
    rm -v /tmp/*.apk && \
    ( /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8 || true ) && \
    echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \
    /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \
    mkdir /opt && \
    curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o /tmp/java.tar.gz \
      http://download.oracle.com/otn-pub/java/jdk/10.0.1+10/fb4372174a714e6b8c52526dc134031e/serverjre-10.0.1_linux-x64_bin.tar.gz && \
    JAVA_PACKAGE_SHA256=$(curl -sSL https://www.oracle.com/webfolder/s/digest/10-0-1checksum.html | grep -E "serverjre-10.0.1_linux-x64_bin\.tar\.gz" | grep -Eo '(sha256: )[^<]+' | cut -d: -f2 | xargs) && \
    echo "${JAVA_PACKAGE_SHA256}  /tmp/java.tar.gz" > /tmp/java.tar.gz.sha256 && \
    sha256sum -c /tmp/java.tar.gz.sha256 && \
    gunzip /tmp/java.tar.gz && \
    tar -C /opt -xf /tmp/java.tar && \
    ln -s /opt/jdk-10.0.1 /opt/jdk  && \
    curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o /tmp/jce_policy-8.zip \
      http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip && \
    cd /tmp && unzip /tmp/jce_policy-8.zip && \
    cp -v /tmp/UnlimitedJCEPolicyJDK8/*.jar /opt/jdk/lib/security/ && \
    apk del curl glibc-i18n && \
    rm -rf /tmp/* /var/cache/apk/* && \
    ln -sf /etc/ssl/certs/java/cacerts $JAVA_HOME/lib/security/cacerts && \
    echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf
