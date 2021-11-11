# Build:
#   docker build -t gbevan/vagrant-ubuntu-dev:latest .
#
# Run:
#  vagrant up --provider=docker
#
# resolve dns issues:
# /etc/conf/docker
#  DOCKER_OPTS="--dns ip_1 --dns ip_2"
#

FROM ubuntu:latest
MAINTAINER Graham Bevan "graham.bevan@ntlworld.com"

ENV DEBIAN_FRONTEND noninteractive
ENV LANG=C
ENV LC_ALL=C

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install -y wget aptitude htop vim git traceroute dnsutils curl ssh sudo psmisc gcc make build-essential pkg-config libglib2.0-dev libpcap-dev libdbi-dev libdbd-pgsql flex sysstat postgresql bison packaging-dev tree && \
    mkdir /var/run/sshd && \
    sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \
    sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config && \
    useradd --create-home -s /bin/bash vagrant && \
    mkdir -p /home/vagrant/.ssh && \
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key" > /home/vagrant/.ssh/authorized_keys && \
    chown -R vagrant: /home/vagrant/.ssh && \
    echo -n 'vagrant:vagrant' | chpasswd && \
    touch /home/vagrant/.hushlogin && \
    mkdir -p /etc/sudoers.d && \
    echo "vagrant ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/vagrant && \
    chmod 0440 /etc/sudoers.d/vagrant && \
    echo "set modeline" > /etc/vim/vimrc.local && \
    echo "export TERM=vt100\nexport LANG=C\nexport LC_ALL=C" > /etc/profile.d/dockenv.sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/usr/sbin/sshd", "-D", "-e"]
EXPOSE 22
