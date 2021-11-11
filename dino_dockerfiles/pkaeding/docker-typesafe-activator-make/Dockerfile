FROM alexanderwink/typesafe-activator
MAINTAINER patrick@kaeding.name

RUN apk update && apk upgrade && apk --no-cache add --update alpine-sdk py-pip nodejs fontconfig ttf-dejavu jq curl
RUN pip install awscli

# https://github.com/AdoptOpenJDK/openjdk-docker/issues/75#issuecomment-469899609
RUN ln -s /usr/lib/libfontconfig.so.1 /usr/lib/libfontconfig.so && \
    ln -s /lib/libuuid.so.1 /usr/lib/libuuid.so.1 && \
    ln -s /lib/libc.musl-x86_64.so.1 /usr/lib/libc.musl-x86_64.so.1
ENV LD_LIBRARY_PATH /usr/lib

ENV PATH="/opt/activator/bin:${PATH}"
