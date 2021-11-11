#use fixed ubuntu version
FROM ubuntu:14.04

#labeling
LABEL maintainer="netiotedge@hilscher.com" \ 
      version="V1.0.0.0" \
      description="NIOT-E-TIJCX-GB passive fieldbus raw data access from container example"

#version
ENV HILSCHERNETIOTEDGE_UBUNTU_SSH_PASSIVE_FIELDBUS_RAW_VERSION 1.0.0.0

#execute all commands as root
USER root

#install SSH 
RUN apt-get update  \
    && apt-get install -y openssh-server

#do users
RUN echo 'root:root' | chpasswd \
    && sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd \
    && mkdir /var/run/sshd 

#copy needed files from repro
COPY "entrypoint.sh" /
RUN chmod +x entrypoint.sh
 
#install essential build environment
RUN apt-get update
RUN apt-get install -y build-essential flex bison

#SSH port
EXPOSE 22 

#setup libnetana for passive access
COPY libnetana/libnetana.so.1.0.2 /usr/lib/
RUN ln -s /usr/lib/libnetana.so.1.0.2 /usr/lib/libnetana.so.1 && ln -s /usr/lib/libnetana.so.1 /usr/lib/libnetana.so && ldconfig

#setup libpcap with support for passive access via libnetana
COPY libpcap/libpcap-1.9.0-netana.tar.gz /tmp/
RUN cd /tmp && tar -xzf libpcap-1.9.0-netana.tar.gz && cd libpcap-1.9.0-netana && ./configure && make && make install && cd /tmp && rm -r *
 
#optional: install tshark but replace libpcap which comes with tshark by our own lib
#          this allows a testrun om the cifXANALYZER_0 device via tshark
RUN apt-get install -y tshark && dpkg -r --force-depends libpcap0.8 && ln -s /usr/local/lib/libpcap.so.1.9.0-netana /usr/lib/x86_64-linux-gnu/libpcap.so.0.8

#set stop signal 
STOPSIGNAL SIGTERM

#the entrypoint is starting ssh
ENTRYPOINT ["/entrypoint.sh"]
