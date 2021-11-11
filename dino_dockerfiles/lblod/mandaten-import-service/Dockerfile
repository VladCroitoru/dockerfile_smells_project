FROM hseeberger/scala-sbt:8u171_2.12.6_1.1.5
RUN apt-get -y update && apt-get -y install cron
COPY import.sh /usr/local/bin/
COPY ttl-importer/ /tmp/ttl-importer/
ENV IMPORT_DIR "/data/imports"
ENV SPARQL_ENDPOINT "http://database:8890/sparql"
ENV DEFAULT_GRAPH "http://mu.semte.ch/application"
ENV CLEAR_ENDPOINT "http://cache/clear"
ENV CRON_PATTERN "30 4 * * *"
RUN cd /tmp/ttl-importer  && sbt assembly && mv target/scala-2.12/ttl-importer-assembly-0.1.0-SNAPSHOT.jar /usr/local/bin/import.jar && rm -rf /tmp/ttl-importer && mkdir -p /data/queries
RUN touch /etc/crontab && chmod 0600 /etc/crontab
CMD printenv | grep -v "no_proxy" >> /etc/environment && echo "$CRON_PATTERN /usr/local/bin/import.sh" > /etc/crontab &&  crontab /etc/crontab && cron -f -L15
