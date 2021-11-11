FROM mwaeckerlin/ubuntu-base
MAINTAINER mwaeckerlin

# icinga API
EXPOSE 5665

# requires: --link mysl:mysql
ENV WEB_USER="icingaweb"
ENV WEB_DB="icingaweb"
ENV WEB_PW=""
ENV DIRECTOR_USER="director"
ENV DIRECTOR_DB="director"
ENV DIRECTOR_PW=""
ENV FEATURES="api checker ido-mysql command checker perfdata graphite"
ENV KEEP_DEFAULTS="0"

RUN apt-get install -y wget debconf-utils pwgen telnet
RUN wget -O - http://packages.icinga.org/icinga.key | apt-key add -
RUN echo "deb http://packages.icinga.org/ubuntu icinga-$(lsb_release -sc) main" > /etc/apt/sources.list.d/icinga-main-trusty.list
RUN apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
      icinga2 icinga2-ido-mysql pwgen openssh-client sudo
RUN sed -i 's,\( *\).*host *=.*,\1host = "carbon",' /etc/icinga2/features-available/graphite.conf
RUN sed -i 's,\( *\).*\(port *=.*\),\1\2,' /etc/icinga2/features-available/graphite.conf

ADD start.sh /start.sh
CMD /start.sh

VOLUME /var/run/icinga2/cmd
VOLUME /var/lib/icinga2
VOLUME /var/lib/nagios
VOLUME /etc/icinga2
