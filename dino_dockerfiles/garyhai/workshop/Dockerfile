FROM centos:6

MAINTAINER Gary Hai "gary@neulinx.com"

# update to latest version of centos6
RUN yum -y update

# install extras repository
RUN yum install epel-release

# install sshd
RUN yum -y install openssh-server
# generate default configuration.
RUN service sshd start
RUN service sshd stop

# very simple password for root
RUN echo "root:firsttime" | chpasswd

# install development envirenment
RUN yum -y install gcc autoconf automake gcc-c++ libtool tar git wget

# install dependencies
RUN yum -y install libev-devel python-devel openssl-devel curl-devel;\
    redis hiredis-devel speex-devel opus-devel
#RUN yum -y install ncurses-devel libuuid-devel libxml2-devel sqlite-devel

# install stable version of libevent2.
RUN mkdir -p /usr/local/src;\
    cd /usr/local/src;\
    wget https://sourceforge.net/projects/levent/files/libevent/libevent-2.0/libevent-2.0.22-stable.tar.gz;\
    tar -zxf libevent-2.0.22-stable.tar.gz;\
    cd libevent-2.0.22-stable;\
    ./configure;\
    make;\
    make install

# install latest release version of XLCP Communications Platform.
RUN mkdir -p /usr/local/src;\
    cd /usr/local/src;\
    git clone https://github.com/neulinx/sems.git sems;\
    cd sems;\
    make;\
    make install

#export ssh server port
EXPOSE 22

CMD /usr/sbin/sshd -D
