
FROM alpine:latest

LABEL author=monlgq  email="monelgq@163.com"

ENV STUNNEL_VER 5.39
ENV STUNNEL_URL https://www.stunnel.org/downloads/stunnel-$STUNNEL_VER.tar.gz
#ENV STUNNEL_SHA256 0ee64774d7a720f3ffd129b08557ee0882704c7f65b859c40e315a175b68a6fd

ENV STUNNEL_FILE stunnel-$STUNNEL_VER.tar.gz
ENV STUNNEL_TEMP stunnel-$STUNNEL_VER-build
# ENV STUNNEL_CONF /usr/local/etc/stunnel/stunnel.conf

ENV STUNNEL_DEPS openssl
ENV BUILD_DEPS curl alpine-sdk openssl-dev

RUN set -xe \
    && apk update \
    && apk add $STUNNEL_DEPS $BUILD_DEPS \
    && mkdir $STUNNEL_TEMP \
        && cd $STUNNEL_TEMP \
        && curl -sSL $STUNNEL_URL -o $STUNNEL_FILE \
        && tar -xf $STUNNEL_FILE --strip 1 \
        && ./configure \
        && make install \
        && cd .. \
        && rm -rf $STUNNEL_TEMP $STUNNEL_FILE \
    && apk --purge del $BUILD_DEPS \
    && mkdir -p /etc/stunnel/

# ADD ./stunnel.conf /etc/stunnel/stunnel.conf

WORKDIR /etc/stunnel 

#RUN chmod 400 userpsk.txt && chmod 400 stunnel.conf

CMD ["stunnel", "/etc/stunnel/stunnel.conf"]
