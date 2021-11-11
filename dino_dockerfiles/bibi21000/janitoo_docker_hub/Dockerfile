FROM debian:jessie

MAINTAINER bibi21000 <bibi21000@gmail.com>

RUN cat /etc/issue
RUN env
RUN /sbin/ip addr

RUN echo "janitoo\njanitoo" | passwd

COPY docker/auto.sh /root/
COPY docker/shell.sh /root/
COPY docker/rescue.sh /root/

RUN apt-get update && \
    apt-get install -y build-essential libwrap0-dev libc-ares-dev python2.7-dev git && \
    apt-get dist-upgrade -y && \
    apt-get install -y sudo openssh-server lxc iptables && \
    mkdir -p /var/run/sshd && \
    apt-get install -y sudo supervisor && \
    mkdir -p /var/log/supervisor && \
    apt-get clean && \
    rm -Rf /root/.cache/*

COPY docker/supervisord.conf /etc/supervisor/

RUN mkdir /opt/janitoo && \
    for dir in src home log run etc init; do mkdir /opt/janitoo/$dir; done && \
    mkdir /opt/janitoo/src/janitoo_docker_hub

ADD . /opt/janitoo/src/janitoo_docker_hub

WORKDIR /opt/janitoo/src/janitoo_docker_hub

RUN make deps && \
    make develop && \
    apt-get clean

RUN apt-get install -y python-pip lm-sensors && \
    pip install psutil bottle batinfo https://bitbucket.org/gleb_zhulik/py3sensors/get/tip.tar.gz && \
    git clone -b develop https://github.com/nicolargo/glances.git && \
    rm -Rf /root/.cache/*

RUN mkdir -p /var/log/docker
RUN /usr/bin/supervisord -c /etc/supervisor/supervisord.conf && make tests

VOLUME /var/lib/docker

CMD ["/root/auto.sh"]
