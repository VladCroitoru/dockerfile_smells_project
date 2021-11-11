FROM alpine
MAINTAINER Arthur Tsang <chiuwai.tsang@hp.com>

ENV JAVA_VERSION 1.8.0_51
ENV ZULU_BUILD 8.8.0.3
ENV ZULU_BUILD_DATE 2015-07-8.8
ENV ZULU_FULL_NAME zulu${JAVA_VERSION}-${ZULU_BUILD}-x86lx64

RUN apk --update add curl && \
    wget "https://circle-artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-2.21-r2.apk" \
         "https://circle-artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-bin-2.21-r2.apk" && \
    apk add --allow-untrusted glibc-2.21-r2.apk glibc-bin-2.21-r2.apk && \
    curl -e http://www.azulsystems.com/products/zulu/downloads\#Linux -o /tmp/jdk.zip http://cdn.azulsystems.com/zulu/${ZULU_BUILD_DATE}-bin/${ZULU_FULL_NAME}.zip && \
    mkdir /opt && unzip -q /tmp/jdk.zip -d /opt && rm /tmp/jdk.zip

RUN ln -s /opt/${ZULU_FULL_NAME}/bin/java /usr/bin/java

ENV JAVA_HOME /opt/${ZULU_FULL_NAME}
ENV PATH ${PATH}:${JAVA_HOME}/bin
