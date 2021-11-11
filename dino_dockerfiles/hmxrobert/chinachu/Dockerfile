FROM centos:latest
MAINTAINER hmxrobert

RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install nodejs npm --enablerepo=epel
RUN yum -y install net-tools wget git unzip bzip2 gcc gcc-c++ make autogen automake kernel-devel patch perl-ExtUtils-MakeMaker libtool openssl-devel libboost-all-dev boost-devel

RUN mkdir -p ~/src
WORKDIR  /root/src
RUN wget http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz
RUN tar xvzf yasm-1.3.0.tar.gz 
WORKDIR /root/src/yasm-1.3.0/
RUN /root/src/yasm-1.3.0/configure
RUN make
RUN make install

RUN npm install rivarun -g

RUN git clone https://github.com/Chinachu/Chinachu /chinachu

WORKDIR /chinachu

RUN echo 1 | /chinachu/chinachu installer

VOLUME ["/mnt/chinachu"]

RUN ln -s /mnt/chinachu/config.json /chinachu/config.json
RUN ln -s /mnt/chinachu/rules.json /chinachu/rules.json

RUN ln -s /mnt/chinachu/recorded /chinachu/recorded
RUN ln -s /mnt/chinachu/data /chinachu/data
RUN ln -s /mnt/chinachu/log /chinachu/log

RUN /chinachu/chinachu service operator initscript > /etc/init.d/chinachu-operator
RUN /chinachu/chinachu service wui initscript > /etc/init.d/chinachu-wui

RUN chmod +x /etc/init.d/chinachu-*

ADD init.sh /
RUN chmod +x /init.sh

EXPOSE 10772 20772

CMD ["/init.sh"]
