FROM ubuntu:14.04

RUN apt-get update

RUN apt-get install -y openssh-server
RUN mkdir -p /var/run/sshd
RUN echo 'root:root' |chpasswd
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor
COPY sshd_nginx_pdnsd.conf /etc/supervisor/conf.d/sshd_nginx_pdnsd.conf

COPY pdnsd /usr/bin/pdnsd
RUN chmod +x /usr/bin/pdnsd
COPY pdnsd.conf /root/pdnsd.conf

COPY nginx /usr/bin/nginx
RUN chmod +x /usr/bin/nginx
COPY nginx.conf /root/nginx.conf

EXPOSE 22 80 53

CMD ["/usr/bin/supervisord"]
