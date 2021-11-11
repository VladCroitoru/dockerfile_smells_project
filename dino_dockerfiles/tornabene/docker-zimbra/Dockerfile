FROM ubuntu:trusty

MAINTAINER Tindaro Tornabene <tindaro.tornabene@gmail.com>

RUN apt-get -y update
RUN apt-get -y install sudo wget tar curl


RUN mkdir /tmp/zcs 
WORKDIR /tmp/zcs

ENV OS UBUNTU14_64
#ENV OS UBUNTU12_64

ENV ZIMBRA zcs-8.0.8_GA_6184.UBUNTU14_64.20140925165809
#ENV ZIMBRA zcs-8.0.7_GA_6021.UBUNTU12_64.20140408123908

RUN wget http://files2.zimbra.com/downloads/8.0.8_GA/$ZIMBRA.tgz
#RUN wget http://files2.zimbra.com/downloads/8.0.7_GA/$ZIMBRA.tgz
#RUN wget  http://10.10.130.35/$ZIMBRA.tgz


WORKDIR /tmp/zcs
RUN tar xzvf $ZIMBRA.tgz
RUN mv $ZIMBRA zcs-install



RUN apt-get -y install openssh-server &&  mkdir /var/run/sshd
RUN apt-get -y install  perl sysstat  hostname libidn11 libpcre3 libexpat1 libgmp3-dev patch pax sqlite3 libaio1 unzip  netcat-openbsd inetutils-ping net-tools 

#install ubuntu 12.04
#RUN apt-get -y install libperl5.14 libgmp3c2


#install ubuntu 14.04
RUN apt-get -y install libperl5.18


RUN locale-gen --no-purge it_IT.UTF-8
ENV LC_ALL it_IT.UTF-8
RUN update-locale LANG=it_IT.UTF-8

ADD config.defaults /tmp/zcs/config.defaults


ADD utilfunc8.0.8.sh /tmp/zcs/utilfunc.sh
#ADD utilfunc8.0.7.sh /tmp/zcs/utilfunc.sh

RUN cp /tmp/zcs/utilfunc.sh /tmp/zcs/zcs-install/util/utilfunc.sh

RUN echo 'root:zimbra' |chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd




WORKDIR /tmp/zcs/zcs-install
RUN pwd
RUN ls
RUN ./install.sh -s --platform-override /tmp/zcs/config.defaults
RUN mv /opt/zimbra /opt/installzimbra


ADD start.sh /start.sh
RUN chmod +x /start.sh

VOLUME ["/home"]
VOLUME ["/opt/zimbra"]


EXPOSE 22
EXPOSE 389
EXPOSE 25
EXPOSE 456
EXPOSE 587
EXPOSE 110
EXPOSE 143
EXPOSE 993
EXPOSE 995
EXPOSE 80
EXPOSE 443
EXPOSE 8080
EXPOSE 8443
EXPOSE 7071


CMD ["/start.sh"]
