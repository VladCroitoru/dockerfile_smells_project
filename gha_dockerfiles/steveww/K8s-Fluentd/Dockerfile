FROM fluentd:v1.14-debian-1

USER root

RUN apt-get update && \
    apt-get install -y build-essential ruby-dev

RUN fluent-gem install fluent-plugin-elasticsearch  && \
    fluent-gem install fluent-plugin-elasticsearch-timestamp-check && \
    fluent-gem install fluent-plugin-splunk-enterprise && \
    fluent-gem install fluent-plugin-kubernetes_metadata_filter && \
    fluent-gem install fluent-plugin-parser-cri && \
    fluent-gem install fluent-plugin-grafana-loki

