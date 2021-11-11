FROM ubuntu:xenial

ARG URL=https://github.com/mdlayher/apcupsd_exporter/releases/download/
ARG VERSION=0.1.0

ENV BUILD_DEPS="wget ca-certificates"

RUN apt-get update \
    && apt-get install -y --no-install-recommends ${BUILD_DEPS} \
    && wget -O /apcupsd_exporter ${URL}/${VERSION}/apcupsd_exporter \
    && chmod +x /apcupsd_exporter \
    && apt-get purge -y ${BUILD_DEPS} \
    && apt-get autoremove -y --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* \
    && rm -rf /usr/share/icons \
    && rm -rf /usr/share/poppler \
    && rm -rf /usr/share/mime \
    && rm -rf /usr/share/GeoIP

ENTRYPOINT ["/apcupsd_exporter"]
