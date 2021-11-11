#
# Derived from https://github.com/cevich/atomic-avahi
#
FROM alpine:3.3
MAINTAINER King-On Yeung <koyeung@gmail.com>

RUN apk add --no-cache avahi
ADD avahi-daemon.conf /etc/avahi/
ADD ssh.service /etc/avahi/services/
ADD avahi-daemon.service /etc/systemd/system/
LABEL RUN /usr/bin/docker run --rm --name NAME --net=host --volume /etc/localtime:/etc/localtime:ro IMAGE /usr/sbin/avahi-daemon --debug
LABEL INSTALL /usr/bin/docker run --privileged --rm --volume /:/host --name NAME IMAGE cp -v /etc/systemd/system/avahi-daemon.service /host/etc/systemd/system/
LABEL UNINSTALL /usr/bin/docker run --privileged --rm --volume /:/host --name NAME IMAGE rm /host/etc/systemd/system/avahi-daemon.service
