FROM ubuntu:12.04
MAINTAINER mose mose@mose.com

ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

RUN apt-mark hold initscripts udev plymouth mountall
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

RUN sed -i 's/main$/main universe/' /etc/apt/sources.list
RUN locale-gen en_US en_US.UTF-8

RUN apt-get -qq update
RUN apt-get -y -qq upgrade
RUN apt-get install -y -qq curl lsb-release supervisor openssh-server cron rsyslog wget
RUN apt-get install -y -qq erlang-nox logrotate

ENV RABBITMQ_VERSION 3.3.0
ENV RABBITMQ_VERSION_MINOR 1
ADD https://www.rabbitmq.com/releases/rabbitmq-server/v${RABBITMQ_VERSION}/rabbitmq-server_${RABBITMQ_VERSION}-${RABBITMQ_VERSION_MINOR}_all.deb /tmp/rabbitmq-server_${RABBITMQ_VERSION}-${RABBITMQ_VERSION_MINOR}_all.deb
RUN dpkg -i /tmp/rabbitmq-server_${RABBITMQ_VERSION}-${RABBITMQ_VERSION_MINOR}_all.deb
RUN rabbitmq-plugins enable rabbitmq_management

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor

RUN echo "root:docker" | chpasswd
RUN mkdir -p /logs/supervisor

ADD files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD files/supervisord-sshd.conf /etc/supervisor/conf.d/sshd.conf
ADD files/supervisord-rsyslogd.conf /etc/supervisor/conf.d/rsyslogd.conf
ADD files/supervisord-rabbitmq.conf /etc/supervisor/conf.d/rabbitmq.conf
ADD files/cron-rsyslog.conf /etc/rsyslog.d/60-cron.conf
ADD files/crontab /etc/crontab

EXPOSE 22 5672 15672

CMD /usr/bin/supervisord -n

