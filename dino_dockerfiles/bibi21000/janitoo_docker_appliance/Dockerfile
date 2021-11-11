FROM python:2.7

MAINTAINER bibi21000 <bibi21000@gmail.com>

ENV JANITOO_DOCKER 1

ENV JANITOO_APPLIANCE_VERSION 14

RUN cat /etc/issue
RUN env
RUN /sbin/ip addr

ENV TERM dumb

RUN echo "janitoo\njanitoo" | passwd

RUN apt-get update && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN apt-get install -y sudo cron openssh-server lsb-release lsb-base apt-transport-https apt-utils && \
    mkdir -p /var/run/sshd && \
    sed -i -e "s/^PermitRootLogin without-password/#PermitRootLogin without-password/" /etc/ssh/sshd_config && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN apt-get install -y sudo supervisor && \
    mkdir -p /var/log/supervisor /etc/supervisor/janitoo.conf.d /etc/supervisor/janitoo-tests.conf.d && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN apt-get install -y git vim-nox nano less && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN apt-get install -y libwrap0-dev libc-ares-dev python2.7-dev python-pip build-essential && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

COPY docker/root/ /root/
COPY docker/supervisord.conf /etc/supervisor/

RUN mkdir /opt/janitoo && \
    for dir in src backups cache home log run etc init; do mkdir /opt/janitoo/$dir; done && \
    mkdir /opt/janitoo/src/janitoo && \
    ln -s /opt/janitoo/log /var/log/janitoo && \
    ln -s /opt/janitoo/etc /etc/janitoo

ADD . /opt/janitoo/src/janitoo_docker_appliance

WORKDIR /opt/janitoo/src

RUN git clone https://github.com/bibi21000/janitoo.git

RUN ln -s janitoo/Makefile.all Makefile && \
    make deps module=janitoo && \
    make install module=janitoo && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN make install module=janitoo_factory && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN make install module=janitoo_factory_exts && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

#RUN apt-get install -y python-pip lm-sensors && \
#    pip install psutil bottle batinfo https://bitbucket.org/gleb_zhulik/py3sensors/get/tip.tar.gz && \
#    cd /root/ && \
#    git clone -b develop https://github.com/nicolargo/glances.git && \
#    apt-get clean && \
#    rm -Rf /root/.cache/* 2>/dev/null||true && \
#    rm -Rf /tmp/* 2>/dev/null||true

CMD ["/root/auto.sh"]
