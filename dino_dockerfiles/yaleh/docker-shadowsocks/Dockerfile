# shadowsocks
#
# VERSION 0.0.1

FROM ubuntu:14.04
MAINTAINER Yale Huang <yale.huang@trantect.com>

RUN apt-get update && \
    apt-get install -y python-pip python-gevent python-m2crypto supervisor \
	openssh-server pen nginx curl
ADD ss_health /usr/local/bin/
RUN pip install shadowsocks==1.4.5 sh
RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor
RUN cat /etc/ssh/sshd_config|sed -e 's/^PermitRootLogin.*/PermitRootLogin yes/' >/etc/ssh/sshd_config
RUN echo 'root:root' | chpasswd
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN echo '*/5 * * * *	root	/usr/local/bin/ss_health' >> /etc/crontab
RUN echo '* * * * *	root	/usr/bin/penctl 127.0.0.1:1990 status >/usr/share/nginx/html/pen.html' >> /etc/crontab
EXPOSE 1989/tcp 1990/tcp 22/tcp 80/tcp
VOLUME ["/etc/supervisor/conf.d"]
VOLUME ["/usr/share/nginx/html"]
CMD ["/usr/bin/supervisord"]

