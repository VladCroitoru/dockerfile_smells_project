FROM python:2.7

MAINTAINER bibi21000 <bibi21000@gmail.com>

ENV JANITOO_DOCKER 1

RUN cat /etc/issue
RUN env
RUN /sbin/ip addr

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

RUN apt-get install -y git vim-nox less && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN apt-get install -y libwrap0-dev libc-ares-dev python2.7-dev && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN apt-get install -y build-essential && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

COPY docker/shell.sh /root/

RUN mkdir /opt/janitoo && \
    for dir in src cache cache/janitoo_manager home log run etc init; do mkdir /opt/janitoo/$dir; done && \
    mkdir /opt/janitoo/src/janitoo && \
    ln -s /opt/janitoo/log /var/log/janitoo && \
    ln -s /opt/janitoo/etc /etc/janitoo

ADD . /opt/janitoo/src/janitoo

WORKDIR /opt/janitoo/src

RUN ln -s janitoo/Makefile.all Makefile && \
    make docker-inst && \
    make deps module=janitoo && \
    make develop module=janitoo && \
    make docker-deps module=janitoo && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN make clone module=janitoo_db && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN make clone module=janitoo_factory && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN make clone module=janitoo_pki && \
    make docker-deps module=janitoo_pki && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN make clone module=janitoo_nginx && \
    make docker-deps module=janitoo_nginx && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN make clone module=janitoo_mosquitto && \
    make docker-deps module=janitoo_mosquitto && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN make clone module=janitoo_mysql && \
    make clone module=janitoo_mysql_client && \
    make -C janitoo_mysql docker-deps && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN make clone module=janitoo_gogs && \
    make -C janitoo_gogs docker-deps && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN make clone module=janitoo_dhcp && \
    make docker-deps module=janitoo_dhcp && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN make clone module=janitoo_layouts && \
    make docker-deps module=janitoo_layouts && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN make clone module=janitoo_events && \
    make clone module=janitoo_events_cron && \
    make clone module=janitoo_events_earth && \
    make docker-deps module=janitoo_events && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN make clone module=janitoo_thermal && \
    make docker-deps module=janitoo_thermal && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN make clone module=janitoo_datalog_rrd && \
    make docker-deps module=janitoo_datalog_rrd && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN make clone module=janitoo_flask && \
    make clone module=janitoo_flask_socketio && \
    make clone module=janitoo_flask_websockets && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN make clone module=janitoo_manager && \
    make clone module=janitoo_manager_proxy && \
    make docker-deps module=janitoo_manager && \
    jnt_dbman initdb -c /opt/janitoo/etc/janitoo_manager.conf && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

RUN apt-get install -y python-pip lm-sensors && \
    pip install psutil bottle batinfo https://bitbucket.org/gleb_zhulik/py3sensors/get/tip.tar.gz && \
    cd /root/ && \
    git clone -b develop https://github.com/nicolargo/glances.git && \
    apt-get clean && \
    rm -Rf /root/.cache/* 2>/dev/null||true && \
    rm -Rf /tmp/* 2>/dev/null||true

CMD ["/root/shell.sh"]
