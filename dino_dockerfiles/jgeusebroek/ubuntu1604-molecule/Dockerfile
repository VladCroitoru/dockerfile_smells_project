FROM ubuntu:xenial
LABEL maintainer="Jeroen Geusebroek"

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
       systemd \
       systemd-cron \
       python2.7 \
       ca-certificates \
       sudo \
    && ln -s /usr/bin/python2.7 /usr/bin/python \
    && rm -Rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean \
    # Disable agetty, fixes zombie agetty 100% cpu.
    # https://github.com/moby/moby/issues/4040
    && cp /bin/true /sbin/agetty

COPY files/initctl_faker .
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker /sbin/initctl

VOLUME [ "/sys/fs/cgroup" ]
CMD [ "/lib/systemd/systemd" ]