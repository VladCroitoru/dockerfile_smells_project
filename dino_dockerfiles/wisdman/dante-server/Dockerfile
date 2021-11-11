FROM alpine:latest

MAINTAINER Wisdman <wisdman@ajaw.it>

ENV DANTE_VER 1.4.2
ENV DANTE_URL https://www.inet.no/dante/files/dante-$DANTE_VER.tar.gz
ENV DANTE_SHA baa25750633a7f9f37467ee43afdf7a95c80274394eddd7dcd4e1542aa75caad
ENV DANTE_FILE dante.tar.gz

RUN set -x \
 && apk --no-cache add bash apg \
 && apk add --no-cache -t .build-deps linux-pam-dev curl gcc g++ make \
 && mkdir -p dante \
 && cd dante \
 && curl -sSL $DANTE_URL -o $DANTE_FILE \
 && echo "$DANTE_SHA *$DANTE_FILE" | sha256sum -c \
 && tar xzf $DANTE_FILE --strip 1 \
 && ac_cv_func_sched_setscheduler=no ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --localstatedir=/var \
    --disable-client \
    --disable-pidfile \
    --without-libwrap \
    --without-pam \
    --without-bsdauth \
    --without-gssapi \
    --without-krb5 \
    --without-upnp \
 && make && make install \
 && cd .. \
 && rm -rf dante \
 && apk del --purge .build-deps \
 && rm -rf /var/cache/apk/* /tmp/*

COPY etc/* /etc/
COPY bin/* /bin/

EXPOSE 1080
CMD ["sockd", "-f", "/etc/sockd.conf", "-N", "10"]
