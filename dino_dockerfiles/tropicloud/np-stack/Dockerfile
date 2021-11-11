FROM centos:centos7
MAINTAINER "Tropicloud" <admin@tropicloud.net>

ADD . /usr/local/nps
RUN /bin/bash /usr/local/nps/np-stack setup

EXPOSE 80 443
ENTRYPOINT ["np","start"]
CMD []
