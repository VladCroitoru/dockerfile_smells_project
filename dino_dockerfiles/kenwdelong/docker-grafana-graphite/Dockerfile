FROM        ubuntu:14.04
MAINTAINER  kenwdelong
# ---------------- #
#   Installation   #
# ---------------- #

# Install all prerequisites
RUN     apt-get update \     
        && apt-get -y install software-properties-common \
        && add-apt-repository -y ppa:chris-lea/node.js \
        && apt-get -y update \
        && apt-get -y install python-django-tagging python-simplejson python-memcache python-ldap python-cairo python-pysqlite2 python-support \
            python-pip gunicorn supervisor nginx-light git wget curl openjdk-7-jre build-essential python-dev libffi-dev \
        && apt-get autoclean \
        && apt-get clean \
        && apt-get autoremove

ENV GRAPHITE_VERSION=1.1.3 \
    STATS_VERSION=v0.8.0 \
    TWISTED_VERSION=18.4.0 \
    GRAFANA_VERSION=5.2.3

RUN     pip install Twisted==$TWISTED_VERSION \
        && pip install pytz
        
RUN	curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - \
    && apt-get install -y nodejs \
	&& npm install -g wizzy

# Checkout the stable branches of Graphite, Carbon and Whisper and install from there
# Install StatsD
RUN     mkdir -p /src \
        && git clone https://github.com/graphite-project/whisper.git /src/whisper \
        && cd /src/whisper \
        && git checkout $GRAPHITE_VERSION \
        && python setup.py install
        
RUN     git clone https://github.com/graphite-project/carbon.git /src/carbon \
        && cd /src/carbon \
        && git checkout $GRAPHITE_VERSION \
        && python setup.py install
        
RUN     git clone https://github.com/graphite-project/graphite-web.git /src/graphite-web \
        && cd /src/graphite-web \
        && git checkout $GRAPHITE_VERSION \
        && python setup.py install \
        && pip install -r requirements.txt \
        && python check-dependencies.py
        
RUN     git clone https://github.com/etsy/statsd.git /src/statsd \
        && cd /src/statsd \
        && git checkout $STATSD_VERSION
        
RUN     mkdir /src/grafana \
        && mkdir /opt/grafana \
        && wget https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana-${GRAFANA_VERSION}.linux-amd64.tar.gz -O /src/grafana.tar.gz \
        && tar -xzf /src/grafana.tar.gz -C /opt/grafana --strip-components=1 \
        && rm /src/grafana.tar.gz

# ----------------- #
#   Configuration   #
# ----------------- #

# Confiure StatsD
ADD     ./statsd/config.js /src/statsd/config.js

# Configure Whisper, Carbon and Graphite-Web
ADD     ./graphite/initial_data.json /opt/graphite/webapp/graphite/initial_data.json
ADD     ./graphite/local_settings.py /opt/graphite/webapp/graphite/local_settings.py
ADD     ./graphite/carbon.conf /opt/graphite/conf/carbon.conf
ADD     ./graphite/storage-schemas.conf /opt/graphite/conf/storage-schemas.conf
ADD     ./graphite/storage-aggregation.conf /opt/graphite/conf/storage-aggregation.conf

RUN     mkdir -p /opt/graphite/storage/whisper \
        && touch /opt/graphite/storage/graphite.db /opt/graphite/storage/index \
        && chown -R www-data /opt/graphite/storage \
        && chmod 0775 /opt/graphite/storage /opt/graphite/storage/whisper \
        && chmod 0664 /opt/graphite/storage/graphite.db \
        && cp /src/graphite-web/webapp/manage.py /opt/graphite/webapp \
        && cd /opt/graphite/webapp/ \
        && python manage.py migrate --run-syncdb --noinput

# Configure Grafana
ADD     ./grafana/custom.ini /opt/grafana/conf/custom.ini

RUN	cd /src \
    && wizzy init \
	&& extract() { cat /opt/grafana/conf/custom.ini | grep $1 | awk '{print $NF}'; } \
	&& wizzy set grafana url $(extract ";protocol")://$(extract ";domain"):$(extract ";http_port")	\		
	&& wizzy set grafana username $(extract ";admin_user")	\
	&& wizzy set grafana password $(extract ";admin_password")
	
# Add the default dashboards
RUN 	mkdir /src/datasources \
        && mkdir /src/dashboards
ADD	    ./grafana/datasources/* /src/datasources
ADD     ./grafana/dashboards/* /src/dashboards/
ADD     ./grafana/export-datasources-and-dashboards.sh /src/

# Configure nginx and supervisord
ADD     ./nginx/nginx.conf /etc/nginx/nginx.conf
ADD     ./supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# ---------------- #
#   Expose Ports   #
# ---------------- #

# Grafana: 80
# StatsD UDP port: 8125
# StatsD Management port: 8126
EXPOSE  80
EXPOSE  8125/udp
EXPOSE  8126

# Elasticsearch data storage path: /var/lib/elasticsearch
# Graphite data storage path: /opt/graphite/storage/whipsper
# Graphite log path: /opt/graphite/storage/log
# Graphite conf path: /opt/graphite/conf
# Supervisor log path: /var/log/supervisor
# VOLUME  ["/var/lib/elasticsearch", "/opt/graphite/storage/whisper", "/opt/graphite/storage/log", "/opt/graphite/conf", "/var/log/supervisor"]

# -------- #
#   Run!   #
# -------- #

CMD     ["/usr/bin/supervisord"]
