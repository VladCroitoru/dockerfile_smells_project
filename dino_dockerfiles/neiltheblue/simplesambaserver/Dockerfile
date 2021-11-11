FROM alpine:3.4

RUN apk --no-cache add samba samba-common-tools

COPY samba.sh samba.sh

EXPOSE 137 139 445 137/udp 138/udp

ENTRYPOINT ["/samba.sh"]
