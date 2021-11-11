FROM ubuntu:latest
MAINTAINER mwaeckerlin

RUN apt-get install -y wget
RUN wget -qO/tmp/install-globaleaks.sh https://deb.globaleaks.org/install-globaleaks.sh
RUN apt-get remove -y wget
RUN chmod +x /tmp/install-globaleaks.sh

EXPOSE 8082
EXPOSE 9040
EXPOSE 9050
VOLUME /etc
VOLUME /var/globaleaks
ADD start.sh /start.sh
CMD /start.sh
