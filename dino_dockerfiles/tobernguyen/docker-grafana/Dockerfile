FROM grafana/grafana:4.3.2

RUN apt-get update && apt-get install -y curl

ADD rootfs /

ARG "version=0.1.0-dev"
ARG "build_date=unknown"
ARG "commit_hash=unknown"
ARG "vcs_url=unknown"
ARG "vcs_branch=unknown"

LABEL org.label-schema.vendor="tobernguyen" \
    org.label-schema.name="Grafana" \
    org.label-schema.description="Grafana with some limited automated data sources creation" \
    org.label-schema.usage="/README.md" \
    org.label-schema.url="https://github.com/tobernguyen/docker-grafana/blob/master/README.md" \
    org.label-schema.vcs-url=$vcs_url \
    org.label-schema.vcs-branch=$vcs_branch \
    org.label-schema.vcs-ref=$commit_hash \
    org.label-schema.version=$version \
    org.label-schema.schema-version="1.0" \
    org.label-schema.docker.cmd.devel="" \
    org.label-schema.docker.params="GF_SECURITY_ADMIN_PASSWORD=Admin user password,\
PROMETHEUS_ENDPOINT=Prometheus address used to obtain data,\
ELASTICSEARCH_ENDPOINT=Elasticsearch addres used to get annotations,\
ELASTICSEARCH_USER=Elasticsearch user,\
ELASTICSEARCH_PASSWORD=Elasticsearch password" \
    org.label-schema.build-date=$build_date

ENV "GF_SECURITY_ADMIN_PASSWORD=admin" \
    "PROMETHEUS_ENDPOINT=http://prometheus:9090" \
    "ELASTICSEARCH_ENDPOINT=http://elasticsearch:9200" \
    "ELASTICSEARCH_USER=readuser" \
    "ELASTICSEARCH_PASSWORD=myelasticpass"

ENTRYPOINT ["/init.sh"]
