FROM phusion/baseimage:latest
MAINTAINER Nicolas Pace <nicolas.pace@unixono.com.ar>

# Set correct environment variables.
ENV HOME /root

# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN apt-get update && \
    apt-get -y install git-core build-essential pkg-config libtool libevent-dev libncurses-dev zlib1g-dev automake libssh-dev cmake ruby wget && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN wget https://github.com/msgpack/msgpack-c/releases/download/cpp-1.3.0/msgpack-1.3.0.tar.gz -O /msgpack-1.3.0.tar.gz && \
    mkdir -p /usr/src/msgpack && tar zxf /msgpack-1.3.0.tar.gz --strip-components 1 -C /usr/src/msgpack && \
    cd /usr/src/msgpack && ./configure --prefix=/usr && make && make install && rm -rf /msgpack-1.3.0.tar.gz /usr/src/msgpack

RUN git clone https://github.com/afirel/tmate-slave.git

RUN cd tmate-slave && \
    ./create_keys.sh && \
    ./autogen.sh && \
    ./configure && \
     make

RUN mkdir /etc/service/tmate-slave
ADD tmate-slave.sh /etc/service/tmate-slave/run

RUN mkdir -p /etc/my_init.d
ADD message.sh /etc/my_init.d/message.sh
