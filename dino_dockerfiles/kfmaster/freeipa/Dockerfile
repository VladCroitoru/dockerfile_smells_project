# Clone from the Fedora 21 image
FROM fedora:21

# Based on Jan Pazdziora from https://github.com/adelton/docker-freeipa.git, slight modified by kfmaster
MAINTAINER kfmaster <fuhaiou@hotmail.com>

# Install FreeIPA server, tolerate rpm error with --skip-broken
RUN mkdir -p /run/lock ; yum install -y deltarpm; yum install -y --skip-broken freeipa-server bind bind-dyndb-ldap perl python-pip && yum clean all

# Replace ADD with COPY, combine multiple RUN together
COPY dbus.service /etc/systemd/system/dbus.service
COPY httpd.service /etc/systemd/system/httpd.service

COPY systemctl /usr/bin/systemctl
COPY systemctl-socket-daemon /usr/bin/systemctl-socket-daemon

COPY ipa-server-configure-first /usr/sbin/ipa-server-configure-first

COPY volume-data-list /etc/volume-data-list
COPY volume-data-mv-list /etc/volume-data-mv-list
COPY add-ipa-user-data.sh /usr/sbin/add-ipa-user-data.sh

RUN ln -sf dbus.service /etc/systemd/system/messagebus.service \
  && chmod -v +x /usr/bin/systemctl /usr/bin/systemctl-socket-daemon /usr/sbin/ipa-server-configure-first /usr/sbin/add-ipa-user-data.sh \
  && groupadd -g 389 dirsrv ; useradd -u 389 -g 389 -c 'DS System User' -d '/var/lib/dirsrv' --no-create-home -s '/sbin/nologin' dirsrv \
  && groupadd -g 17 pkiuser ; useradd -u 17 -g 17 -c 'CA System User' -d '/var/lib' --no-create-home -s '/sbin/nologin' pkiuser \
  && /usr/bin/pip install shyaml \
  && cd / ; mkdir /data-template ; cat /etc/volume-data-list | while read i ; do if [ -e $i ] ; then tar cf - .$i | ( cd /data-template && tar xf - ) ; fi ; mkdir -p $( dirname $i ) ; rm -rf $i ; ln -sf /data${i%/} ${i%/} ; done \
  && mv /data-template/etc/dirsrv/schema /usr/share/dirsrv/schema && ln -s /usr/share/dirsrv/schema /data-template/etc/dirsrv/schema \
  && echo 0.5 > /etc/volume-version \
  && uuidgen > /data-template/build-id 

EXPOSE 53/udp 53 80 443 389 636 88 464 88/udp 464/udp 123/udp 7389 9443 9444 9445

VOLUME /data

ENTRYPOINT /usr/sbin/ipa-server-configure-first
