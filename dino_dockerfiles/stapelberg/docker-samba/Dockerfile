FROM debian:jessie
MAINTAINER Michael Stapelberg <michael+nas@stapelberg.ch>

RUN apt-get update && apt-get install -y samba

ADD smb.conf /etc/samba/smb.conf

EXPOSE 137 138 139 445
CMD ["/usr/sbin/smbd", "-FS"]
