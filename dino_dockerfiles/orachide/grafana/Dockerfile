FROM grafana/grafana

MAINTAINER Rachide Ouattara (orachide)

#Install curl to access Grafana HTTP API
#Install jq to to parse *json file
RUN apt-get update \
    && apt-get -y --no-install-recommends install curl jq \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && true

COPY ./run_grafana.sh /run_grafana.sh

COPY ./configure_datasources.sh /configure_datasources.sh

VOLUME ["/etc/grafana/datasources"]

RUN chmod +x /*.sh

ENTRYPOINT ["/run_grafana.sh"]

