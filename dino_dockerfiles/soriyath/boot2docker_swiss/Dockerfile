FROM boot2docker/boot2docker
Maintainer Sumi Straessle

# Add configuration files (swiss ntp servers, swiss timezone)
ADD ntpd $ROOTFS/etc/rc.d/ntpd
ADD Zurich $ROOTFS/etc/localtime

RUN chmod 755 $ROOTFS/etc/rc.d/ntpd

ENV DOCKER_STORAGE=overlay

RUN $ROOTFS/tmp/make_iso.sh
CMD ["sh", "-c", "[ -t 1 ] && exec bash || exec cat boot2docker.iso"]