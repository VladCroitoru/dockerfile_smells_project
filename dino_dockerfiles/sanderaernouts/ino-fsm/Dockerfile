# Docker container for FullScreenMario server
# http://www.fullscreenmario.com


FROM centos:centos6
MAINTAINER Chris Collins <collins.christopher@gmail.com>

# https://github.com/FullScreenShenanigans/FullScreenMario.git removed - DMCA
ENV FSM https://github.com/dignifiedquire/FullScreenMario.git

RUN yum install -y httpd git && yum clean all
RUN git clone $FSM /var/www/fsm
RUN rmdir /var/www/html && ln -s /var/www/fsm /var/www/html

EXPOSE 80

ENTRYPOINT [ "/usr/sbin/httpd", "-DFOREGROUND" ]

