FROM alpine:3.12.1

COPY --chown=100:101 rootfs /

RUN apk add --no-cache clamav rsyslog clamav-libunrar && \
    mkdir /clamav /run/clamav && \
    chown clamav:clamav /clamav /run/clamav && \
    chmod +x /start.sh && \
    rm -rf /apk /tmp/* /var/cache/apk/*

USER clamav

CMD ["/start.sh"]
