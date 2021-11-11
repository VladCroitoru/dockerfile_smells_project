FROM debian:jessie

MAINTAINER peter@c3re.de

RUN apt-get -y update

RUN apt-get -y install nano netcat rsyslog wget dbus less dialog
RUN cd ; wget -O - https://github.com/andryyy/mailcow/archive/v0.14.tar.gz | tar xfz -

COPY install_mailcow.sh /root/mailcow-0.14/
RUN chmod 777 /root/mailcow-0.14/install_mailcow.sh

COPY dienste_starten.sh /root/mailcow-0.14/
RUN chmod 777 /root/mailcow-0.14/dienste_starten.sh

COPY mailcow.config     /root/mailcow-0.14/
COPY functions.sh       /root/mailcow-0.14/includes/


RUN cd /root/mailcow-0.14 && ./install_mailcow.sh

CMD /bin/bash
CMD /root/mailcow-0.14/dienste_starten.sh
