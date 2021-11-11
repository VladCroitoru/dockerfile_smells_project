FROM bibi21000/janitoo

MAINTAINER bibi21000 <bibi21000@gmail.com>

ENV JNTD_VERSION 1

RUN cat /etc/issue
RUN env
RUN /sbin/ip addr

RUN mkdir /opt/janitoo/src/janitoo_docker_stable/

ADD . /opt/janitoo/src/janitoo_docker_stable

RUN date +'%Y/%m/%d %H:%M:%S'

WORKDIR /opt/janitoo/src

VOLUME ["/root/.ssh/", "/etc/nginx/conf.d/", "/var/log", "/etc/mosquitto/", "/var/lib/mosquitto/", "/etc/supervisor/", "/opt/janitoo/home/", "/opt/janitoo/etc/", "/opt/janitoo/src/"]

EXPOSE 22 1883 5005 8080 8085 8086 9001

CMD ["/root/auto.sh"]
