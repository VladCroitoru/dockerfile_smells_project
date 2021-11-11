FROM ubuntu

RUN apt-get update && apt-get install -y \
        cron \
        software-properties-common \
    && rm -rf /var/lib/apt/lists/*

RUN add-apt-repository ppa:maxmind/ppa
RUN apt-get update && apt-get install -y \
        geoipupdate \
    && rm -rf /var/lib/apt/lists/*

VOLUME /usr/share/GeoIP

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["cron"]
