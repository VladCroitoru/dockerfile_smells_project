############################################################
# Dockerfile: CentOS7 & transmission
############################################################
FROM centos:centos7

MAINTAINER CarbonSphere <CarbonSphere@gmail.com>

# Set environment variable
ENV HOME 						/root
ENV TERM 						xterm

RUN yum -y update; yum -y install epel-release; yum -y clean all

RUN yum -y install transmission transmission-daemon

EXPOSE 9091
RUN mkdir -p /root/.config/transmission-daemon; chown -R transmission:transmission /root/.config
RUN mkdir /Downloads ; chown -R transmission:transmission /Downloads
VOLUME ["/Downloads"]
VOLUME ["/root/.config/transmission-daemon"]
ADD start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

CMD ["start.sh"]
