#
# Dockerfile for Odoo-Maintenance Shell
#
# Based on instructions from https://github.com/tutumcloud/tutum-ubuntu/
#
FROM ubuntu:lucid
MAINTAINER Stephen Garran <stephen@insoproco.com>

ENV AUTHORIZED_KEYS **None**
ENV INSTANCE_VOLUME  /var/lib/odoo

# Install packages
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install openssh-server pwgen
RUN mkdir -p /var/run/sshd && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config

ADD set_root_pw.sh /set_root_pw.sh
ADD run.sh /run.sh
RUN chmod +x /*.sh

VOLUME ["${INSTANCE_VOLUME}"]

EXPOSE 22
CMD ["/run.sh"]

