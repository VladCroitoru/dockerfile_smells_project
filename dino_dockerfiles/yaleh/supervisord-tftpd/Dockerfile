FROM ubuntu:12.04
MAINTAINER Yale Huang <yale.huang@trantect.com>

RUN apt-get install -y curl
RUN apt-get update
RUN apt-get install -y openssh-server supervisor tftpd-hpa
RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor
RUN echo 'root:root' | chpasswd
ADD run /usr/local/bin/
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 22 69/udp
VOLUME ["/var/lib/tftpboot"]
CMD ["/usr/bin/supervisord"]
