FROM ubuntu:18.04
### Set up SystemD
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
    dbus systemd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN systemctl set-default multi-user.target

RUN echo '#!/bin/sh \n\
set -eu \n\
mkdir -p /host/sys/fs/cgroup/systemd || true \n\
nsenter --mount=/host/proc/1/ns/mnt -- mount -t cgroup cgroup -o none,name=systemd /sys/fs/cgroup/systemd' > /sbin/setup

STOPSIGNAL SIGRTMIN+3

# Workaround for docker/docker#27202, technique based on comments from docker/docker#9212
CMD ["/bin/bash", "-c", "exec /sbin/init --log-target=journal 3>&1"]

### Set up SSH
EXPOSE 22

RUN apt-get update && apt-get install -y openssh-server
RUN rm -rf /etc/ssh/ssh_host*

RUN echo '[Unit] \n\
Description=Generate SSH host keys \n\
Before=ssh.service \n\
[Service] \n\
Type=oneshot \n\
ExecStart=/bin/bash -c "test -f /etc/ssh/ssh_host_dsa_key || dpkg-reconfigure openssh-server" \n\
[Install] \n\
RequiredBy=ssh.service' > /etc/systemd/system/ssh-host-key.service

RUN chmod 664 /etc/systemd/system/ssh-host-key.service
RUN systemctl enable ssh-host-key.service

RUN mkdir /root/.ssh && \
  touch /root/.ssh/authorized_keys && \
  chmod 700 /root/.ssh && \
  chmod 600 /root/.ssh/authorized_keys

### Add Vagrant
# Add Vagrant key
RUN mkdir -p /root/.ssh && \
    echo 'ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key' > /root/.ssh/authorized_keys && \
    chmod 700 /root/.ssh && \
    chmod 644 /root/.ssh/authorized_keys

# Set a gross default root password
RUN echo 'root:root' | chpasswd

# Install some bare minimal Ansible items
run apt-get -y install apt-transport-https python-minimal

# Add environment to allow things like PIP to work
ENV LANG C
