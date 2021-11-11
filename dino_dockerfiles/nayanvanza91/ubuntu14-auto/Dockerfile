from ubuntu:14.04

MAINTAINER Nayan V. <nayanvanza91@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install -y language-pack-en-base \
    && locale-gen en_US.UTF-8 \
    && export LANG=en_US.UTF-8 \
    && LC_ALL=en_US.UTF-8 \
    && apt-get update \
    && apt-get install -y software-properties-common \
    && apt-get install -y python-software-properties \
    && apt-get install -y build-essential \
    && apt-get install -y rsyslog \
    && apt-get install -y vim \
    && apt-get install -y tcl8.5 \
    && apt-get install -y cron \
    && apt-get install -y curl \
    && apt-get install -y rsync \
    && apt-get install -y git \
    && apt-get install -y psmisc \
    && apt-get install -y apt-transport-https \
    && apt-get install -y supervisor \
    && apt-get install -y openssh-server \
    && mkdir /var/run/sshd \
    && sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config 

ADD tools/docker/supervisor/supervisord.conf /etc/supervisor/supervisord.conf
ADD tools/docker/supervisor/conf.d/apps.conf /etc/supervisor/conf.d/apps.conf

#ADD tools/docker/scripts/entrypoint.sh /entrypoint.sh
ADD tools/docker/scripts/start.sh /start.sh

RUN chmod +x /*.sh

EXPOSE 22 80 443 3306 8080 9200

#ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
CMD ["/bin/bash", "/start.sh"]
