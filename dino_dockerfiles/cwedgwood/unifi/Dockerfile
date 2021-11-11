# -*- conf -*-

# We want/need stretch as that has mongodb 3.x and the java 8 which
# both work; more recent jre and mongodb will not work
FROM debian:stretch-slim

# debian:stretch-slim lacks this, needed or alternates throws errors
RUN mkdir -p /usr/share/man/man1/


# BASE SYSTEM

# setup users/groups (to be consistent); ideally we want something
# like:
#
#   mongodb:x:42001:42001::/var/lib/mongodb:/bin/false
#   unifi:x:42002:42002::/var/lib/unifi:/bin/false

# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=858903
#RUN useradd -d /var/lib/mongodb -M -s /bin/false -u 42001 -U mongodb
RUN useradd -d /var/lib/unifi -M -s /bin/false -u 42002 -U unifi

# *required* to make unifi happy: binutils libcap2 procps (for pgrep),
# *required*/useful (and small): wget, less
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
        apt-get install -y --no-install-recommends mongodb-server jsvc openjdk-8-jre-headless binutils libcap2 procps wget less curl iproute2 logrotate && \
    apt-get clean && \
    find /var/lib/apt/lists/ -type f -print0 | xargs -r0 rm && \
    rm -vrf /tmp/hsperf*

# mongodb uid fixup hack (see above)
RUN find / -xdev -user mongodb -print0 | xargs -r0 chown -v 42001:42001 && \
    sed -i "s/^\(mongodb:x\).*::/\1:42001:42001::/" /etc/passwd && \
    sed -i "s/^\(mongodb:x\).*/\1:42001:/" /etc/group

# ADD UNIFI CONTROLLER

#ARG UNIFI_DEB_URL=https://please.pass.in.location.of.deb
# This is duplicated right now because of a DockerHub quirk
ARG UNIFI_DEB_URL=https://dl.ui.com/unifi/6.2.26/unifi_sysvinit_all.deb

RUN cd / && \
    wget -q $UNIFI_DEB_URL && \
    DEBIAN_FRONTEND=noninteractive dpkg -i /unifi_sysvinit_all.deb && \
    rm /unifi_sysvinit_all.deb


# Suggested but maybe not entirely useful
EXPOSE 6789/tcp 8080/tcp 8443/tcp 8880/tcp 8843/tcp 3478/udp


# Checked by startup script to make make sure volumes are supplied
RUN touch /var/log/unifi/not-supplied /var/lib/unifi/not-supplied

COPY unifi-start.sh unifi-stop.sh /usr/lib/unifi/
RUN ln -s /usr/lib/unifi/unifi-start.sh /entrypoint.sh && \
    ln -s /usr/lib/unifi/unifi-stop.sh /stop.sh

RUN cd /usr/lib/unifi && \
        ln -s /run/unifi run && \
	ln -s /var/lib/unifi/ data && \
	ln -s /var/log/unifi logs

# if we exec' in, it's useful to see we've done so as in most cases
# the hostname won't have changed
ENV debian_chroot="Unifi Controller"

USER unifi
CMD [ "/usr/lib/unifi/unifi-start.sh" ]
