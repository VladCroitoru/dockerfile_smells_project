FROM registry.dryusdan.fr/dryusdan/php:7.1


ARG VERSION=3.3.0
ARG GPG_matthieu="814E 346F A01A 20DB B04B  6807 B5DB D592 5590 A237"

ENV UID=991 GID=991 \
    UPLOAD_MAX_SIZE=10M \
    MEMORY_LIMIT=512M \
    OPCACHE_MEM_SIZE=256M

RUN BUILD_DEPS=" \
    git \
    tar \
    build-base \
    autoconf \
    geoip-dev \
    libressl \
    ca-certificates \
    gnupg" \
 && apk -U upgrade && apk add \
    ${BUILD_DEPS} \
    geoip \
    tzdata \
    python2 \
 && pecl install geoip-1.1.1 \
 && echo 'extension=geoip.so' >> /php/conf.d/geoip.ini \
 && mkdir /piwik && cd /tmp \
 && PIWIK_TARBALL="piwik-${VERSION}.tar.gz" \
 && wget -q https://builds.piwik.org/${PIWIK_TARBALL} \
 && wget -q https://builds.piwik.org/${PIWIK_TARBALL}.asc \
 && wget -q https://builds.piwik.org/signature.asc \
 && echo "Verifying authenticity of ${PIWIK_TARBALL}..." \
 && gpg --import signature.asc \
 && FINGERPRINT="$(LANG=C gpg --verify ${PIWIK_TARBALL}.asc ${PIWIK_TARBALL} 2>&1 \
  | sed -n "s#Primary key fingerprint: \(.*\)#\1#p")" \
 && if [ -z "${FINGERPRINT}" ]; then echo "Warning! Invalid GPG signature!" && exit 1; fi \
 && if [ "${FINGERPRINT}" != "${GPG_matthieu}" ]; then echo "Warning! Wrong GPG fingerprint!" && exit 1; fi \
 && echo "All seems good, now unpacking ${PIWIK_TARBALL}..." \
 && tar xzf ${PIWIK_TARBALL} --strip 1 -C /piwik \
 && wget -q https://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz -P /usr/share/GeoIP/ \
 && gzip -d /usr/share/GeoIP/GeoLiteCity.dat.gz \
 && mv /usr/share/GeoIP/GeoLiteCity.dat /usr/share/GeoIP/GeoIPCity.dat \
 && git clone https://github.com/matomo-org/matomo-log-analytics.git /tmp/mamoto-log-analytics \
 && mv /tmp/mamoto-log-analytics/import_logs.py /piwik/ \
 && apk del ${BUILD_DEPS} php7-dev php7-pear \
 && rm -rf /tmp/*  /var/cache/apk/* /tmp/* /root/.gnupg /root/.cache/

COPY rootfs /

RUN chmod +x /usr/local/bin/startup /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*

VOLUME ["/config", "/logs"]

EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/startup"]
CMD ["/bin/s6-svscan", "/etc/s6.d"]
