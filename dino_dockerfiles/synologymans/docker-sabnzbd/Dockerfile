FROM ubuntu:16.04
MAINTAINER cybermans <cybermans@gmail.com>
LABEL version 20180313

RUN echo "deb http://archive.ubuntu.com/ubuntu xenial multiverse" >> /etc/apt/sources.list 
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:jcfp/ppa && \
    add-apt-repository -y ppa:jcfp/sab-addons && \
    add-apt-repository -y ppa:mosquitto-dev/mosquitto-ppa && \
    apt-get update && \
    apt-get install -y sabnzbdplus locales && \ 
    #apt-get install -y sabnzbdplus-theme-classic sabnzbdplus-theme-mobile sabnzbdplus-theme-plush \ &&
    apt-get install -y par2-tbb python-yenc python-pip unzip rar mosquitto-clients && \
    apt-get -y autoremove && \
    apt-get -y clean

RUN echo 149 | dpkg-reconfigure locales
RUN echo "LANG=en_US.utf8" >> /etc/default/locale
RUN pip install sabyenc --upgrade
RUN mkdir -p /config && \
    mkdir -p /data

EXPOSE 8080 9090

VOLUME ["/config"]
VOLUME ["/data"]

ENV LANG=en_US.UTF-8

ENTRYPOINT ["/usr/bin/sabnzbdplus"]
CMD ["--config-file","/config","--server",":8080","--console"]
