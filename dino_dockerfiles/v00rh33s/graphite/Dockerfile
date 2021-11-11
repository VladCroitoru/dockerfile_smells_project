FROM ubuntu:14.04.2

ENV DEBIAN_FRONTEND noninteractive

ADD src src

RUN apt-get update && \
    apt-get install -y wget graphite-web graphite-carbon supervisor && \
    cp src/local_settings.py /etc/graphite/local_settings.py && \
    cp src/initial_data.json /etc/graphite/initial_data.json && \
    cd /etc/graphite; graphite-manage syncdb --noinput; cd / && \
    sed -ri 's/CARBON_CACHE_ENABLED=false/CARBON_CACHE_ENABLED=true/'g /etc/default/graphite-carbon && \
    sed -ri 's/ENABLE_LOGROTATION = False/ENABLE_LOGROTATION = True/'g /etc/carbon/carbon.conf && \
    cp src/storage-schemas.conf /etc/carbon/storage-schemas.conf && \
    cp /usr/share/doc/graphite-carbon/examples/storage-aggregation.conf.example /etc/carbon/storage-aggregation.conf && \
    apt-get install -y apache2 libapache2-mod-wsgi && \
    a2dissite 000-default && \
    cp /usr/share/graphite-web/apache2-graphite.conf /etc/apache2/sites-available && \
    a2ensite apache2-graphite && \
    service apache2 start && \
    service apache2 reload && \
    service apache2 stop && \
    chown -R _graphite:_graphite /var/log/graphite/ && \
    chown -R _graphite:_graphite /var/lib/graphite/ && \
    chmod +w /var/lib/graphite/graphite.db && \
    mkdir -p /var/log/supervisor && \
    cp src/supervisord.conf /etc/supervisor/conf.d/supervisord.conf && \
    apt-get autoclean && \
    rm -rf /src && \
    rm -rf /var/lib/apt/lists/*

#   80 - Graphite Django Interface
# 2003 - Carbon Line Receiver
# 2004 - Carbon Pickle Receiver
# 7002 - Carbon Cache
EXPOSE 80 2003 2004 7002

VOLUME /var/log/graphite /var/lib/graphite/whisper

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
