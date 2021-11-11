FROM tutum/debian:wheezy

ENV DEBIAN_FRONTEND noninteractive
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Base system setup
RUN apt-get -qq update \
    && apt-get -yqq upgrade \
    && apt-get -yqq install apt-utils locales locales-all vim mc curl wget less python-pip supervisor \
    && pip install supervisor-stdout

ADD base/locale /etc/default/locale
ADD base/supervisord.conf /etc/supervisor/supervisord.conf
ADD base/sv_stdout.conf /etc/supervisor/conf.d/

# Container setup
RUN apt-get -qqy remove dbconfig-common \
    && apt-get -qqy install --no-install-recommends bash sudo procps ca-certificates wget supervisor mysql-client apache2 pwgen unzip php5-mysql php-apc less
RUN wget --quiet -O - http://packages.icinga.org/icinga.key | apt-key add - \
    && echo "deb http://packages.icinga.org/debian icinga-wheezy-snapshots main" >> /etc/apt/sources.list \
    && echo "deb http://httpredir.debian.org/debian wheezy-backports main" >> /etc/apt/sources.list
RUN apt-get -qq update \
    && apt-get -qqy install --no-install-recommends libjs-jquery-ui/wheezy-backports \
    && apt-get -qqy install --no-install-recommends icinga2 icinga2-ido-mysql nagios-plugins icingaweb2

ADD content/ /

RUN mkdir /icinga2 \
    && mkdir /icingaweb2

RUN chmod u+x /opt/supervisor/icinga2_supervisor /opt/supervisor/apache2_supervisor /opt/run

# Temporary hack to get icingaweb2 modules via git
RUN mkdir -p /etc/icingaweb2/enabledModules \
    && wget --quiet --no-cookies --no-check-certificate "https://github.com/Icinga/icingaweb2/archive/master.zip" -O /tmp/icingaweb2.zip \
    && unzip -qq /tmp/icingaweb2.zip "icingaweb2-master/modules/doc/*" "icingaweb2-master/modules/monitoring/*" -d "/tmp/icingaweb2" \
    && cp -R /tmp/icingaweb2/icingaweb2-master/modules/monitoring /etc/icingaweb2/modules/ \
    && cp -R  /tmp/icingaweb2/icingaweb2-master/modules/doc /etc/icingaweb2/modules/ \
    && rm -rf /tmp/icingaweb2.zip /tmp/icingaweb2

EXPOSE 80 22

VOLUME  ["/icinga2", "/icingaweb2"]

# Initialize and run Supervisor
ENTRYPOINT ["/opt/run"]
