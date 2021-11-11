FROM phusion/baseimage:0.9.19

MAINTAINER Mask Wang, mask.wang.cn@gmail.com

# Ensure UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8

ENV HOME /root

# enable ssh
RUN rm -f /etc/service/sshd/down
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Enabling the insecure key permanently
RUN /usr/sbin/enable_insecure_key

CMD ["/sbin/my_init"]

# Replace APT Source
#ADD build/sources.list /etc/apt/sources.list

RUN apt-get update --fix-missing
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y vim curl wget build-essential python-software-properties\
 cmake telnet nmap

ADD build/QConf-1.2.0.tar.gz /tmp/
RUN cd /tmp/ && \
	cd QConf-1.2.0 && \
	mkdir build && cd build && \
	cmake .. && make && make install

RUN mkdir -p        /etc/service/qconf
ADD build/qconf.sh /etc/service/qconf/run
RUN chmod +x        /etc/service/qconf/run

#EXPOSE 80

#RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
