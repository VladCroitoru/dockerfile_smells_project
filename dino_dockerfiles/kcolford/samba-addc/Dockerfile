FROM base/archlinux
RUN pacman -Syu --noconfirm samba
VOLUME /var/lib/samba/private /var/lib/samba/sysvol /etc/samba
EXPOSE 53/tcp 53/udp 88/tcp 88/udp 135/tcp 137/udp 138/udp 139/tcp 389/tcp 389/udp 445/tcp 464/tcp 464/udp 636/tcp 3268/tcp 3269/tcp 49152/tcp
ENV REALM example.com
ENV DOMAIN example
CMD [ -e /etc/samba/smb.conf ] || samba-tool domain provision --use-rfc2307 --realm $REALM --domain $DOMAIN; samba --foreground
