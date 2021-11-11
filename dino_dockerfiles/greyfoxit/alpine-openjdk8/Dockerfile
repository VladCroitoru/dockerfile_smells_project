FROM greyfoxit/alpine-glibc:alpine3.6_glibc2.26

# maintainer: Greyfox Team | team@greyfox.it | @greyfoxit

ENV JAVA_HOME=/usr/lib/jvm/default-jvm \
    JAVA_VERSION=8u131 \
    JAVA_ALPINE_VERSION=8.131.11-r2

ENV PATH=$PATH:$JAVA_HOME/jre/bin:$JAVA_HOME/bin \
    LANG=C.UTF-8

RUN apk add --no-cache openjdk8="$JAVA_ALPINE_VERSION"
