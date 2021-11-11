FROM docker.io/scico/easybuildor:centos7

ENV EBDIR /opt/apps

ENV LMOD_VER 6.5.2
ENV EASYBUILD_PREFIX ${EBDIR}
ENV EASYBUILD_MODULES_TOOL Lmod

MAINTAINER Lars Melwyn <melwyn (at) scico.io>

USER root
RUN echo -e " \n\
[easyrepo] \n\
name=EasyBuild repo \n\
baseurl=http://46.101.150.132/centos/7.2.1511/os/x86_64 \n\
enabled=yes \n\
gpgcheck=0" > /etc/yum.repos.d/easyrepo.repo

RUN yum -y update && yum -y install master  && yum clean all && chown -R apps.apps /opt/apps

USER apps

CMD /bin/bash
