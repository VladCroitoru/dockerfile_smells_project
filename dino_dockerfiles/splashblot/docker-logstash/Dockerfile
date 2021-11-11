FROM logstash:5-alpine

ARG "version=0.1.0-dev"
ARG "build_date=unknown"
ARG "commit_hash=unknown"
ARG "vcs_url=unknown"
ARG "vcs_branch=unknown"

LABEL org.label-schema.vendor="Softonic" \
    org.label-schema.name="Logstash" \
    org.label-schema.description="Logstash with outputs for ES in 3 different indexes: access, alerts and logs." \
    org.label-schema.usage="/src/README.md" \
    org.label-schema.url="https://github.com/bvis/docker-logstash/blob/master/README.md" \
    org.label-schema.vcs-url=$vcs_url \
    org.label-schema.vcs-branch=$vcs_branch \
    org.label-schema.vcs-ref=$commit_hash \
    org.label-schema.version=$version \
    org.label-schema.schema-version="1.0" \
    org.label-schema.docker.cmd.devel="" \
    org.label-schema.docker.params="DEBUG=Activate all logs in stdout,\
ELASTICSEARCH_SSL=Elasticsearch endpoint is under HTTPS,\
ELASTICSEARCH_USER=Elasticsearch User,\
ELASTICSEARCH_PASSWORD=Elasticsearch password,\
ELASTICSEARCH_ADDR=Elasticsearch address,\
ELASTICSEARCH_PORT=Elasticserach port" \
    org.label-schema.build-date=$build_date


ENV "ELASTICSEARCH_ADDR=elasticsearch" \
    "ELASTICSEARCH_PORT=9200"

ADD rootfs /

CMD ["-f", "/config-dir/"]
