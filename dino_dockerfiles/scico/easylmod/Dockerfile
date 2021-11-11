FROM centos:7.5.1804

ENV LMOD_VER 7.8.2
ENV LMODDIR /opt/apps

MAINTAINER Lars Melwyn <melwyn (at) scico.io>

RUN  yum -y install epel-release && yum -y update && yum -y install git tar which bzip2 xz \
     bash-completion make automake unzip  patch python-keyring lua lua-devel lua-posix lua-filesystem tcl \
     iproute gcc gcc-c++ zlib-devel openssl-devel sudo &&  yum clean all

RUN useradd -u 1000 -d /home/apps apps && usermod -a -G wheel apps && echo '%wheel ALL=(ALL)       NOPASSWD: ALL'>>/etc/sudoers


RUN mkdir -p ${LMODDIR}/build && chown -R apps.apps ${LMODDIR}

USER apps
WORKDIR ${LMODDIR}/build
RUN curl -LO http://github.com/TACC/Lmod/archive/${LMOD_VER}.tar.gz && \ 
    mv ${LMODDIR}/build/${LMOD_VER}.tar.gz ${LMODDIR}/build/Lmod-${LMOD_VER}.tar.gz && \ 
    tar xvf Lmod-${LMOD_VER}.tar.gz

WORKDIR ${LMODDIR}/build/Lmod-${LMOD_VER}
RUN ./configure --prefix=${LMODDIR}/software/Lmod && make install 

USER root
RUN  ln -s ${LMODDIR}/software/Lmod/lmod/lmod/init/profile /etc/profile.d/modules.sh  && \
     ln -s ${LMODDIR}/software/Lmod/lmod/lmod/init/cshrc /etc/profile.d/modules.csh

USER apps 
WORKDIR /home/apps

CMD /bin/bash
