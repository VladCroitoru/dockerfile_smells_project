FROM centos
MAINTAINER moremagic <itoumagic@gmail.com>
RUN yum -y update
RUN yum install -y passwd openssh-server initscripts

RUN echo 'root:root' | chpasswd
RUN /usr/sbin/sshd-keygen

#emacs, etc install
RUN yum -y install emacs vim wget curl tar
ADD resource/emacs/init.el /root/.emacs.d/

#gaushe install
RUN yum -y install make gcc
RUN cd /tmp/ && \
    wget http://prdownloads.sourceforge.net/gauche/Gauche-0.9.4.tgz && \
    tar zxvf Gauche-0.9.4.tgz && \
    cd Gauche-0.9.4 && \
    ./configure && make && make install && \
    rm -rf /tmp/*

EXPOSE 22
CMD /usr/sbin/sshd -D
