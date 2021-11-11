FROM debian:latest

MAINTAINER Jacky "https://github.com/haoasdasdf/debian-ssh"

RUN apt-get update && \
	apt-get install -y openssh-server && \
	apt-get clean

RUN echo 'root:root' |chpasswd

RUN sed -ri 's/^#\s*PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
	sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN mkdir -p /var/run/sshd

EXPOSE 80 22 443 9999 10000 10001 12595

# My custom
WORKDIR /root/

RUN echo 'deb http://ftp.jp.debian.org/debian/ stretch main' > /etc/apt/sources.list
RUN echo 'deb-src http://ftp.jp.debian.org/debian/ stretch main' >> /etc/apt/sources.list
RUN echo 'deb http://security.debian.org/debian-security stretch/updates main' >> /etc/apt/sources.list
RUN echo 'deb-src http://security.debian.org/debian-security stretch/updates main' >> /etc/apt/sources.list

RUN mkdir -p /root/.ssh
RUN touch /root/.ssh/authorized_keys

RUN apt-get update && apt-get install  git nano supervisor curl wget cron screen python-pip python3-pip -y 

# Config Supervisor and sshd
RUN apt-get install -y supervisor
RUN touch /etc/supervisor/conf.d/sshd.conf
RUN echo '[program:sshd]' >> /etc/supervisor/conf.d/sshd.conf
RUN echo 'command=/usr/sbin/sshd -D' >> /etc/supervisor/conf.d/sshd.conf
RUN echo 'autorestart=true' >> /etc/supervisor/conf.d/sshd.conf

RUN sed -i "s/\/var\/run/\/dev\/shm/g" /etc/supervisor/supervisord.conf

ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]