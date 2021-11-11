# @edt ASIX M11 Curs 2017-2018
# hostservices:base
# Docker amb serveis de xarxa engegats
# ---------------------------------------------------------

FROM fedora:24
MAINTAINER @isx45128227 "Roger Ferran @edt Curs 2017-2018"

RUN dnf -y update vi
RUN dnf -y install vim iputils iproute procps mlocate man-db nmap tree \
                   uw-imap sendmail tftp tftp-server vsftpd httpd telnet telnet-server openssh openssh-server openssh-clients \
                   policycoreutils ftp
RUN mkdir /opt/docker/
COPY sendmail.sh /opt/docker/
COPY startup.sh /opt/docker/

RUN chmod +x /opt/docker/startup.sh /opt/docker/sendmail.sh

#COPY dades/index.html /var/www/html
#COPY dades/index.html dades/README.txt /var/ftp/pub/
ADD dades.tar.gz /opt/docker/

RUN cp /opt/docker/prova/README.txt /var/ftp/pub/
RUN cp /opt/docker/prova/index.html /var/www/html/

COPY dades/index.html dades/README.md /var/lib/tftpboot/
COPY xinetd/* /etc/xinetd.d/

RUN /usr/bin/ssh-keygen -A

EXPOSE 19 13 9 7 2080 143 993 110 995 37 2222 2007 2013 20 21 69 23 80 22

CMD ["/opt/docker/startup.sh"]


