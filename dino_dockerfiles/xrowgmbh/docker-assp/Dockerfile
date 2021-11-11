#Creating Images for ASSP web service 
FROM jamesarems/assp:beta
MAINTAINER James PS <jamesarems@gmail.com>

#Updating CentOS packages

COPY ./start.sh /usr/bin/
RUN rm -rf /usr/share/assp/assp.pl
COPY ./assp.pl /usr/share/assp/assp.pl
RUN chmod +x /usr/bin/start.sh

#Exposing tcp ports
EXPOSE 2220
EXPOSE 125
EXPOSE 25

#Adding volume
VOLUME /usr/share/assp
VOLUME /etc/postfix/

#Running final script
ENTRYPOINT ["/usr/bin/start.sh"]
