FROM ubuntu:14.04
MAINTAINER ondrej@hamada.cz

# Update of system and installation of Graphite
RUN apt-get update && apt-get upgrade -y && \
    echo 'graphite-carbon  graphite-carbon/postrm_remove_databases boolean false' | debconf-set-selections && \
    apt-get install --no-install-recommends -y graphite-web graphite-carbon apache2 libapache2-mod-wsgi python-psycopg2 supervisor curl postgresql-client


# Configure Graphite
ADD ./graphite/storage-schemas.conf /etc/carbon/storage-schemas.conf
ADD ./graphite/carbon.conf /etc/carbon/carbon.conf
ADD ./graphite/local_settings.py /etc/graphite/local_settings.py
ADD ./graphite/run-carbon /usr/sbin/run-carbon
RUN sed -i 's/^CARBON_CACHE_ENABLED=.*$/CARBON_CACHE_ENABLED=true/' /etc/default/graphite-carbon && \
    cp /usr/share/graphite-web/apache2-graphite.conf /etc/apache2/sites-available && \
    sed -i 's/\*:80>/\*:8080>/' /etc/apache2/sites-available/apache2-graphite.conf && \
    echo 'Listen 8080' >> /etc/apache2/ports.conf && \
    a2dissite 000-default && a2ensite apache2-graphite

# Install Grafana
RUN echo 'deb https://packagecloud.io/grafana/stable/debian wheezy main' >> /etc/apt/sources.list && \
    curl -k https://packagecloud.io/gpg.key | apt-key add - && \
    apt-get install --no-install-recommends -y --force-yes apt-transport-https adduser libfontconfig && \
    curl -k -O https://grafanarel.s3.amazonaws.com/builds/grafana_2.6.0_amd64.deb && \
    dpkg -i grafana_2.6.0_amd64.deb && \
    rm -f grafana_2.6.0_amd64.deb

# Configure Grafana
ADD ./grafana/grafana.ini /etc/grafana/grafana.ini
ADD ./grafana/apache2-grafana.conf /etc/apache2/sites-available/apache2-grafana.conf
ADD ./grafana/run-grafana /usr/sbin/run-grafana
RUN a2enmod proxy proxy_http xml2enc && \
    a2ensite apache2-grafana && \
    chown :grafana /etc/grafana/grafana.ini
ADD ./scripts/run_graphite_grafana.sh /usr/sbin/run_graphite_grafana.sh
ADD ./supervisord/graphite-grafana.conf /etc/supervisor/conf.d/graphite-grafana.conf

# Ports
#   80 - Grafana
# 8080 - Graphite
# 2003 - Carbon
# 2004 - Carbon
# 7002 - Carbon

EXPOSE 80 8080 2003 2004 7002

CMD [ "/usr/sbin/run_graphite_grafana.sh" ]
