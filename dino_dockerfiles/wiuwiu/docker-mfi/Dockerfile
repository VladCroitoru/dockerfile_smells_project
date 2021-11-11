# docker image
FROM lsiobase/xenial

# environment settings
ARG DEBIAN_FRONTEND="noninteractive"

# install packages
RUN \
  echo "deb http://dl.ubnt.com/mfi/distros/deb/debian debian ubiquiti" >> /etc/apt/sources.list && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50 && \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y  software-properties-common && \
  add-apt-repository ppa:webupd8team/java -y && \
  apt-get update && \
  echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
  apt-get install -y \
   oracle-java7-installer \
   mongodb-server \
   mfi \
   wget && \

# cleanup
apt-get clean && \
rm -rfv /tmp/* /var/lib/apt/lists/* /var/tmp/*

# add local files
COPY root/ /

# volumes
WORKDIR /usr/lib/mfi
VOLUME /config

# ports
EXPOSE 2323/tcp 6080/tcp 6443/tcp 6843/tcp 6880/tcp
EXPOSE 1900/udp 3478/udp 10001/udp
