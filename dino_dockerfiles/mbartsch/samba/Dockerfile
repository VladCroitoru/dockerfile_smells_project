# https://github.com/letsencrypt/letsencrypt/pull/431#issuecomment-103659297
# it is more likely developers will already have ubuntu:trusty rather
# than e.g. debian:jessie and image size differences are negligible
FROM alpine:3.7
MAINTAINER Marcelo Bartsch <spam-mb+github@bartsch.cl>

RUN apk --no-cache add samba samba-common-tools cups dbus avahi bash && rm -f /var/cache/apk/* && sed -i 's#/bin/ash#/bin/bash#'  /etc/passwd && adduser -S -D smbuser && rm -f /etc/avahi/services/* && touch /etc/printcap
COPY smbd.service /etc/avahi/services/
COPY smb.conf /etc/samba/smb.conf
COPY samba.sh /samba.sh
RUN chmod +x /samba.sh
ENTRYPOINT [ "/samba.sh" ]
EXPOSE "137/tcp" "137/udp" "139/tcp" "445/tcp" 
HEALTHCHECK CMD smbclient -L localhost -N
