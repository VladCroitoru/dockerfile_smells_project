FROM debian:buster
MAINTAINER brettm357@me.com

ARG BUILD_DATE
ARG VERSION=6.5.45
LABEL build_version="brettm357 version:- ${VERSION} Build-date:- ${BUILD_DATE}"

    # SET ENVIROMENT VARIABLES
ENV DEBIAN_FRONTEND noninteractive
ENV UNIFI_VERSION 6.5.45-c8122c1151

    # INSTALL PACKAGES
RUN echo "deb http://ftp.us.debian.org/debian stretch main" \
    | tee -a /etc/apt/sources.list.d/stretch.list && \
    apt-get update -q && \
    apt-get upgrade -y && \
    apt-get dist-upgrade -y && \
    apt-get -y install --no-install-recommends \
      binutils \
      curl \
      jsvc \
      libcap2 \
      logrotate \
      mongodb-server \
      openjdk-8-jre-headless \
      prelink \
      supervisor \
      wget && \        
    # INSTALL UNIFI    
    wget -nv https://dl.ui.com/unifi/$UNIFI_VERSION/unifi_sysvinit_all.deb && \    
    dpkg --install unifi_sysvinit_all.deb && \
    rm unifi_sysvinit_all.deb && \
    apt-get -y purge wget && \    
    # FIX WEBRTC STACK GUARD ERROR 
    execstack -c /usr/lib/unifi/lib/native/Linux/x86_64/libubnt_webrtc_jni.so && \
    apt-get -y purge prelink && \    
    apt-get -q clean && \ 
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*.deb /tmp/* /var/tmp/*
    
    # FORWARD PORTS
EXPOSE 3478/udp 6789/tcp 8080/tcp 8081/tcp 8443/tcp 8843/tcp 8880/tcp 8883/tcp 

    # SET INTERNAL STORAGE VOLUME
VOLUME ["/usr/lib/unifi/data"]

    # SET WORKING DIRECTORY FOR PROGRAM
WORKDIR /usr/lib/unifi

    # ADD SUPERVISOR CONFIG
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord","--configuration=/etc/supervisor/supervisord.conf"]

