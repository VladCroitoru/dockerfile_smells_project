FROM linuxserver/baseimage

MAINTAINER Sparklyballs <sparklyballs@linuxserver.io>

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Add local files
ADD src/ /

# repositories
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty main universe restricted' > /etc/apt/sources.list && \
echo 'deb http://archive.ubuntu.com/ubuntu trusty-updates main universe restricted' >> /etc/apt/sources.list && \

# install dependencies
apt-get update && \ 
apt-get install -y \
python3 \
python3-pip && \
firefox && \
xserver-xephyr && \
xvfb && \
zlib1g-dev && \

# clean up
apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#VOLUME
VOLUME /code
