FROM qnib/alplain-init

ENV QCOLLECT_GRAPHITE_INTERVAL=4 \
    QCOLLECT_INTERVAL=4 \
    QCOLLECT_INTERNAL_SERVER_PORT=29090 \
    QCOLLECT_PORT=19191 \
    QCOLLECT_PREFIX=qcollect \
    QCOLLECT_GRAPHITE_ENABLED=false \
    QCOLLECT_GRAPHITE_INTERVAL=4 \
    QCOLLECT_GRAPHITE_PREFIX_DIMENSIONS=false \
    QCOLLECT_GRAPHITE_SERVER=carbon \
    QCOLLECT_INFLUXDB_ENABLED=false \
    QCOLLECT_INFLUXDB_SERVER=influxdb \
    QCOLLECT_INFLUXDB_PORT=8086 \
    QCOLLECT_INFLUXDB_INTERVAL=4 \
    QCOLLECT_INFLUXDB_USERNAME=root \
    QCOLLECT_INFLUXDB_PASSWORD=root \
    QCOLLECT_INFLUXDB_DATABASE=qcollect \
    QCOLLECT_OPENTSDB_COLLECTOR_ENABLED=true \
    QCOLLECT_OPENTSDB_PORT=4242 \
    QCOLLECT_DOCKERSTATS_CPUTHROTTLE=false \
    QCOLLECT_DOCKERSTATS_CPUPERCORE=false \
    QCOLLECT_DOCKERSTATS_BLKIO=true \
    QCOLLECT_DOCKERSTATS_SKIP_REGEX="[a-z]+_[a-z]+\$"

RUN apk add --no-cache nmap bc jq openssl \
 && wget -qO /usr/local/bin/go-github https://github.com/qnib/go-github/releases/download/0.2.2/go-github_0.2.2_MuslLinux \
 && chmod +x /usr/local/bin/go-github \
 && echo "# $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo qcollect --limit 1 --regex '.*_alpine$')" \
 && wget -qO /usr/bin/qcollect $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo qcollect --limit 1 --regex ".*_alpine$") \
 && chmod +x /usr/bin/qcollect \
 && rm -rf /var/cache/apk/* /usr/local/bin/go-github
ADD opt/qnib/qcollect/bin/start.sh \
    opt/qnib/qcollect/bin/healthcheck.sh \
    opt/qnib/qcollect/bin/warn.sh \
    /opt/qnib/qcollect/bin/
ADD opt/qnib/entry/30-config-qcollect.sh \
    opt/qnib/entry/31-config-qcollect-opentsdb.sh \
    /opt/qnib/entry/
ADD opt/qnib/qcollect/etc/DockerStats.conf \
    opt/qnib/qcollect/etc/OpenTSDB.conf \
    opt/qnib/qcollect/etc/qcollect.conf \
    /opt/qnib/qcollect/etc/
CMD ["/opt/qnib/qcollect/bin/start.sh"]
