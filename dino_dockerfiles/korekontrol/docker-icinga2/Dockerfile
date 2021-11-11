# Dockerfile for icinga2 with icingaweb2
# https://github.com/korekontrol/docker-icinga2

FROM debian:buster

ENV APACHE2_HTTP=REDIRECT \
    ICINGA2_FEATURE_GRAPHITE=false \
    ICINGA2_FEATURE_GRAPHITE_HOST=graphite \
    ICINGA2_FEATURE_GRAPHITE_PORT=2003 \
    ICINGA2_FEATURE_GRAPHITE_URL=http://graphite \
    ICINGA2_USER_FULLNAME="Icinga2" \
    ICINGA2_FEATURE_DIRECTOR="true" \
    ICINGA2_FEATURE_DIRECTOR_KICKSTART="true" \
    ICINGA2_FEATURE_DIRECTOR_USER="icinga2-director" \
    DEBIAN_FRONTEND="noninteractive"


RUN  echo "deb http://deb.debian.org/debian stretch-backports main" /etc/apt/sources.list.d/stretch-backports.list \
     && apt-get -qy update \
     && apt-get install -qy --no-install-recommends \
          apache2 \
          apt-transport-https \
          bc \
          ca-certificates \
          curl \
          dirmngr \
          dnsutils \
          gnupg \
#          openjdk-8-jre-headless \
          openjdk-11-jre-headless \
          jq \
          lsb-release \
          mailutils \
          mariadb-client \
          php-curl \
          php-ldap \
          php-mysql \
          php7.3-opcache \
          procps \
          pwgen \
          snmp \
#          ssmtp \
          sudo \
          supervisor \
          unzip \
          wget \
     && curl -s https://packages.icinga.com/icinga.key | apt-key add - \
     && echo "deb http://packages.icinga.org/debian icinga-$(lsb_release -cs) main" > /etc/apt/sources.list.d/icinga2.list \
     && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 10779AB4 \
     && echo "deb https://raw.githubusercontent.com/nisabek/icinga2-slack-notifications/master/reprepro general main" > /etc/apt/sources.list.d/icinga2-slack.list \
     && apt-get update \
     && apt-get install -y --no-install-recommends \
          icinga2 \
          icinga2-bin \
          icinga2-ido-mysql \
          icinga2-slack-notifications \
          icingacli \
          icingaweb2 \
          monitoring-plugins \
          nagios-nrpe-plugin \
          nagios-snmp-plugins \
          nagios-plugins-contrib \
     && apt-get -qy install python-pip python-six python-pyasn1 python-requests python-pbr python-redis python-pika python-awsauth \
     && pip install awscli \
     && pip install python-jenkins \
     && pip install 'elasticsearch>=5.0.0,<6.0.0' \
     && apt-get -qy remove python-pip \
     && apt-get -qy autoremove \
     && apt-get clean \
     && rm -rf /var/lib/apt/lists/*

RUN wget -O /usr/lib/nagios/plugins/check_cloudwatch_metrics https://raw.githubusercontent.com/rizvir/check_cloudwatch_metrics/master/check_cloudwatch_metrics \
     && chmod 755 /usr/lib/nagios/plugins/check_cloudwatch_metrics

RUN wget -O /tmp/opsgenie.deb https://s3-us-west-2.amazonaws.com/opsgeniedownloads/repo/opsgenie-icinga2_2.15.0_all.deb \
     && dpkg -i /tmp/opsgenie.deb \
     && rm -f /tmp/opsgenie.deb


# Temporary hack to get icingaweb2 modules via git
ARG GITREF_IPL=stable/0.4.0
ARG GITREF_INCUBATOR=stable/0.5.0
ARG GITREF_REACTBUNDLE=stable/0.7.0
ARG GITREF_ICINGAWEB2=master
ARG GITREF_DIRECTOR=master
ARG GITREF_MODGRAPHITE=master
ARG GITREF_MODAWS=master
ARG GITREF_MODELASTICSEARCH=master
ARG GITREF_MODBUSINESSPROCESS=master
ARG GITREF_MODCUBE=master



RUN mkdir -p /usr/local/share/icingaweb2/modules/ \
    && wget -q --no-cookies -O - "https://github.com/Icinga/icingaweb2/archive/${GITREF_ICINGAWEB2}.tar.gz" \
    | tar xz --strip-components=2 --directory=/usr/local/share/icingaweb2/modules -f - icingaweb2-${GITREF_ICINGAWEB2}/modules/monitoring icingaweb2-${GITREF_ICINGAWEB2}/modules/doc \
# Icinga ipl
    && mkdir -p /usr/local/share/icingaweb2/modules/ipl/ \
    && wget -q --no-cookies -O - "https://github.com/Icinga/icingaweb2-module-ipl/archive/${GITREF_IPL}.tar.gz" \
    | tar xz --strip-components=1 --directory=/usr/local/share/icingaweb2/modules/ipl --exclude=.gitignore -f - \
# Icinga incubator
    && mkdir -p /usr/local/share/icingaweb2/modules/incubator/ \
    && wget -q --no-cookies -O - "https://github.com/Icinga/icingaweb2-module-incubator/archive/${GITREF_INCUBATOR}.tar.gz" \
    | tar xz --strip-components=1 --directory=/usr/local/share/icingaweb2/modules/incubator --exclude=.gitignore -f - \
# Icinga reactbundle
    && mkdir -p /usr/local/share/icingaweb2/modules/reactbundle/ \
    && wget -q --no-cookies -O - "https://github.com/Icinga/icingaweb2-module-reactbundle/archive/${GITREF_REACTBUNDLE}.tar.gz" \
    | tar xz --strip-components=1 --directory=/usr/local/share/icingaweb2/modules/reactbundle --exclude=.gitignore -f - \
# Icinga Director
    && mkdir -p /usr/local/share/icingaweb2/modules/director/ \
    && wget -q --no-cookies -O - "https://github.com/Icinga/icingaweb2-module-director/archive/${GITREF_DIRECTOR}.tar.gz" \
    | tar xz --strip-components=1 --directory=/usr/local/share/icingaweb2/modules/director --exclude=.gitignore -f - \
# Icingaweb2 Graphite
    && mkdir -p /usr/local/share/icingaweb2/modules/graphite \
    && wget -q --no-cookies -O - "https://github.com/Icinga/icingaweb2-module-graphite/archive/${GITREF_MODGRAPHITE}.tar.gz" \
    | tar xz --strip-components=1 --directory=/usr/local/share/icingaweb2/modules/graphite -f - icingaweb2-module-graphite-${GITREF_MODGRAPHITE}/ \
# Icingaweb2 Elasticsearch
    && mkdir -p /usr/local/share/icingaweb2/modules/elasticsearch \
    && wget -q --no-cookies -O - "https://github.com/Icinga/icingaweb2-module-elasticsearch/archive/${GITREF_MODELASTICSEARCH}.tar.gz" \
    | tar xz --strip-components=1 --directory=/usr/local/share/icingaweb2/modules/elasticsearch -f - icingaweb2-module-elasticsearch-${GITREF_MODGRAPHITE}/ \
# Icingaweb2 Business Process
    && mkdir -p /usr/local/share/icingaweb2/modules/businessprocess \
    && wget -q --no-cookies -O - "https://github.com/Icinga/icingaweb2-module-businessprocess/archive/${GITREF_MODBUSINESSPROCESS}.tar.gz" \
    | tar xz --strip-components=1 --directory=/usr/local/share/icingaweb2/modules/businessprocess -f - icingaweb2-module-businessprocess-${GITREF_MODBUSINESSPROCESS}/ \
# Icingaweb2 Cube
    && mkdir -p /usr/local/share/icingaweb2/modules/cube \
    && wget -q --no-cookies -O - "https://github.com/Icinga/icingaweb2-module-cube/archive/${GITREF_MODCUBE}.tar.gz" \
    | tar xz --strip-components=1 --directory=/usr/local/share/icingaweb2/modules/cube -f - icingaweb2-module-cube-${GITREF_MODCUBE}/ \
# Icingaweb2 AWS
    && mkdir -p /usr/local/share/icingaweb2/modules/aws \
    && wget -q --no-cookies -O - "https://github.com/korekontrol/icingaweb2-module-aws/archive/${GITREF_MODAWS}.tar.gz" \
    | tar xz --strip-components=1 --directory=/usr/local/share/icingaweb2/modules/aws -f - icingaweb2-module-aws-${GITREF_MODAWS}/ \
    && wget -q --no-cookies "https://github.com/aws/aws-sdk-php/releases/download/2.8.30/aws.zip" \
    && unzip -d /usr/local/share/icingaweb2/modules/aws/library/vendor/aws aws.zip \
    && rm aws.zip


COPY content/ /

# Final fixes
RUN true \
    && sed -i 's/vars\.os.*/vars.os = "Docker"/' /etc/icinga2/conf.d/hosts.conf \
    && mv /etc/icingaweb2/ /etc/icingaweb2.dist \
    && mkdir /etc/icingaweb2 \
    && mv /etc/icinga2/ /etc/icinga2.dist \
    && mkdir /etc/icinga2 \
    && usermod -aG icingaweb2 www-data \
    && usermod -aG nagios www-data \
    && rm -rf \
        /var/lib/mysql/* \
    && chmod u+s,g+s \
        /bin/ping \
        /bin/ping6 \
        /usr/lib/nagios/plugins/check_icmp 

EXPOSE 80 443 5665

# Initialize and run Supervisor
ENTRYPOINT ["/opt/run"]
