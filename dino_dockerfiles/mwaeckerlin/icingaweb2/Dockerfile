FROM mwaeckerlin/ubuntu-base
MAINTAINER mwaeckerlin

# requires: --link mysql:mysql
ENV TIMEZONE "Europe/Zurich"
ENV WEBROOT ""
ENV GRAPHITE_WEB "http://graphite"

RUN apt-get update -y && apt-get install -y wget nmap
RUN wget -O - http://packages.icinga.org/icinga.key | apt-key add -
RUN echo "deb http://packages.icinga.org/ubuntu icinga-$(lsb_release -sc) main" > /etc/apt/sources.list.d/icinga-main-trusty.list
RUN apt-get update -y && apt-get install -y icingaweb2 libapache2-mod-php php-curl git
RUN git clone https://github.com/Icinga/icingaweb2-module-director.git /usr/share/icingaweb2/modules/director
RUN git clone https://github.com/Icinga/icingaweb2-module-graphite /usr/share/icingaweb2/modules/graphite
RUN mkdir -p /etc/icingaweb2/modules/graphite
# graphite to be fixed
#RUN cp -rv /usr/share/icingaweb2/modules/graphite/sample-config/icinga2/* /etc/icingaweb2/modules/graphite/
RUN chown -R root:icingaweb2 /etc/icingaweb2/modules/graphite
RUN chmod -R 2755 /etc/icingaweb2/modules/graphite
#RUN sed -i "s,web_url = .*,web_url = ${GRAPHITE_WEB}," /etc/icingaweb2/modules/graphite/config.ini
RUN a2dissite 000-default
ADD apache.conf /etc/apache2/sites-available/icingaweb2.conf
RUN a2ensite icingaweb2

ADD start.sh /start.sh
CMD /start.sh

EXPOSE 80
VOLUME /etc/icingaweb2
VOLUME /var/log/icingaweb2
