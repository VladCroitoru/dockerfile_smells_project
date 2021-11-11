FROM alpine:3.8

LABEL description="A minimalist, open source online pastebin where the server has zero knowledge of pasted data" \
      maintainer="Hardware <contact@meshup.net>"

ARG VERSION=1.2.1
ARG GPG_FINGERPRINT="28CA 7C96 4938 EA5C 1481  D42A E11B 7950 E9E1 83DB"
ARG SHA256_HASH="d3489ebe5f82463ed01eda4d8c195f8ce1e4730743f67617b90f07b629896332"

ENV GID=991 UID=991 UPLOAD_MAX_SIZE=10M

RUN echo "@community https://nl.alpinelinux.org/alpine/v3.8/community" >> /etc/apk/repositories \
 && apk -U upgrade \
 && apk add -t build-dependencies \
    gnupg \
    openssl \
    wget \
    ca-certificates \
 && apk add \
    musl \
    nginx \
    s6 \
    su-exec \
    php7-fpm@community \
    php7-gd@community \
    php7-mcrypt@community \
    php7-json@community \
    php7-zlib@community \
 && cd /tmp \
 && wget -q https://github.com/PrivateBin/PrivateBin/archive/${VERSION}.zip \
 && wget -q https://github.com/PrivateBin/PrivateBin/releases/download/${VERSION}/PrivateBin-${VERSION}.zip.asc \
 && wget -q https://privatebin.info/key/release.asc \
 && gpg --import release.asc \
 && echo "Verifying both integrity and authenticity of ${VERSION}.zip..." \
 && CHECKSUM=$(sha256sum ${VERSION}.zip | awk '{print $1}') \
 && if [ "${CHECKSUM}" != "${SHA256_HASH}" ]; then echo "ERROR: Checksum does not match!" && exit 1; fi \
 && FINGERPRINT="$(LANG=C gpg --verify PrivateBin-${VERSION}.zip.asc ${VERSION}.zip 2>&1 \
  | sed -n "s#Primary key fingerprint: \(.*\)#\1#p")" \
 && if [ -z "${FINGERPRINT}" ]; then echo "ERROR: Invalid GPG signature!" && exit 1; fi \
 && if [ "${FINGERPRINT}" != "${GPG_FINGERPRINT}" ]; then echo "ERROR: Wrong GPG fingerprint!" && exit 1; fi \
 && echo "All seems good, now unpacking ${VERSION}.zip..." \
 && mkdir /privatebin && unzip -q /tmp/${VERSION}.zip -d /privatebin \
 && mv /privatebin/PrivateBin-${VERSION}/* /privatebin && rm -rf /privatebin/PrivateBin-${VERSION}/ \
 && mv /privatebin/cfg/conf.sample.php /privatebin/conf.php \
 && apk del build-dependencies \
 && rm -rf /var/cache/apk/* /tmp/* /root/.gnupg

COPY rootfs /
RUN chmod +x /usr/local/bin/run.sh /services/*/run /services/.s6-svscan/*
VOLUME /privatebin/cfg /privatebin/data
EXPOSE 8888
CMD ["run.sh"]
