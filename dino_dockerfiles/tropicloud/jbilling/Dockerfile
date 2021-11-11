FROM tornabene/docker-ntipa-base
MAINTAINER Tropicloud <admin@tropicloud.net>

RUN apt-get -y install vim git zip unzip bzip2
RUN apt-get -y install sudo wget
WORKDIR /opt
RUN wget http://ufpr.dl.sourceforge.net/project/jbilling/jbilling%20Latest%20Stable/jbilling-3.3.1/jbilling-community-3.3.1.zip
RUN unzip jbilling-community-3.3.1.zip
WORKDIR /opt/jbilling-community-3.3.1/bin
ADD jbilling.sh /opt/jbilling-community-3.3.1/bin/jbilling.sh
ADD jbilling.conf /etc/supervisor/conf.d/jbilling.conf
RUN chmod +x *.sh

EXPOSE 8080
CMD /usr/bin/supervisord