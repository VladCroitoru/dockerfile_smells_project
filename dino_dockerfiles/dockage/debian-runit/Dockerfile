FROM dockage/debian:latest
MAINTAINER Mohammad Abdoli Rad <m.abdolirad@gmail.com>

STOPSIGNAL SIGCONT

ENV SERVICE_AVAILABLE_DIR=/etc/sv \
    SERVICE_ENABLED_DIR=/service

ENV SVDIR=${SERVICE_ENABLED_DIR} \
    SVWAIT=7

ADD https://cdn.rawgit.com/dockage/runit-scripts/f994f02f/scripts/installer /opt/
RUN apt-get update \
    && apt-get install -y runit \
    && mkdir -p ${SERVICE_AVAILABLE_DIR} ${SERVICE_ENABLED_DIR} \
    && chmod +x /opt/installer \
    && /opt/installer \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /opt/installer

ENTRYPOINT ["/sbin/runit-init"]
