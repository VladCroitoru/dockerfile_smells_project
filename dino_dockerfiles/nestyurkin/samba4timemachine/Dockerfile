FROM alpine

ARG BUILD_DATE
LABEL org.label-schema.build-date=$BUILD_DATE org.label-schema.schema-version="1.0"

RUN apk --no-cache --no-progress upgrade && \
    apk --no-cache --no-progress add bash samba shadow tini && \
    adduser -D -G users -H -S -g 'Samba User' -h /tmp smbuser \
    && rm -rf /var/cache/apk/* \
    && rm -rf /tmp/*

COPY smb.conf /etc/samba/
COPY samba.sh /usr/bin/

EXPOSE 137/udp 138/udp 139 445

#HEALTHCHECK --interval=60s --timeout=15s CMD smbclient -L '\\localhost\' -U 'guest%' -m SMB3

VOLUME ["/etc/samba"]
VOLUME ["/srv"]

ENTRYPOINT ["/sbin/tini", "--", "/usr/bin/samba.sh"]
