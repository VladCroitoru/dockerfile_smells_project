FROM khezen/elasticsearch:6

RUN /run/miscellaneous/restore_config.sh && \
    /elasticsearch/bin/elasticsearch-plugin install -b ingest-geoip && \
    /elasticsearch/bin/elasticsearch-plugin install -b ingest-user-agent && \
    cp -r elasticsearch/config/ingest-geoip /.backup/elasticsearch/config/ && \
    rm -rf /elasticsearch/config/* && \
    echo "rsync -av --ignore-existing /.backup/elasticsearch/config/ingest-geoip/ /elasticsearch/config/ingest-geoip/" >> /run/miscellaneous/restore_config.sh
