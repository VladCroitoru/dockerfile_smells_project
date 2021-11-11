FROM ubuntu:16.04

ENV container docker

# Don't start any optional services except for the few we need.
RUN find /etc/systemd/system \
    /lib/systemd/system \
    -path '*.wants/*' \
    -not -name '*journald*' \
    -not -name '*systemd-tmpfiles*' \
    -not -name '*systemd-user-sessions*' \
    -exec rm \{} \;

RUN apt-get update && \
    apt-get install -y \
    dbus curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN systemctl set-default multi-user.target


RUN curl -L -o /usr/local/bin/gosu https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64 && chmod +x /usr/local/bin/gosu
RUN curl -L -o /usr/local/bin/goss https://github.com/aelsabbahy/goss/releases/download/v0.3.5/goss-linux-amd64 && chmod +x /usr/local/bin/goss

HEALTHCHECK --interval=1s --timeout=6s CMD goss -g /goss/goss.yaml validate

RUN mkdir goss && cd goss && goss -g /goss/goss.yaml autoadd gosu

# Add base entrypoint script for sub images to point to
COPY docker-entrypoint.sh /usr/local/bin/

RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat

COPY setup /sbin/

STOPSIGNAL SIGRTMIN+3

# Workaround for docker/docker#27202, technique based on comments from docker/docker#9212
CMD ["/bin/bash", "-c", "exec /sbin/init --log-target=journal 3>&1"]