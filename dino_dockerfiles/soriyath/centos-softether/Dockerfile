FROM soriyath/centos-swissfr
MAINTAINER Sumi Straessle

# SoftEther build dependencies
RUN yum install -y binutils chkconfig zlib binutils readline openssl ncurses libevent ncurses-devel openssl-devel readline-devel

# Compile SoftEther
WORKDIR /usr/local/src
RUN git clone --depth=1 https://github.com/SoftEtherVPN/SoftEtherVPN.git
WORKDIR /usr/local/src/SoftEtherVPN
RUN ./configure <<< $'1\n2\n' \
	&& make -j $(cat /proc/cpuinfo | grep processor | wc -l) \
	&& make install \
	&& cd .. \
	&& rm -rf SoftEtherVPN
WORKDIR /

ADD softether.sv.conf /etc/supervisor/conf.d/softether.sv.conf
ADD softether.sh /usr/local/src/softether.sh
RUN chmod 700 /usr/local/src/softether.sh

# Clean container
RUN yum -y clean all \
	&& yum -y autoremove \
	&& rm -rf ~/.cache/pip/*

EXPOSE 1194/udp 5555/tcp 1701/tcp 4500/udp 500/udp

# default command
CMD ["supervisord", "-c", "/etc/supervisor/supervisor.conf"]
