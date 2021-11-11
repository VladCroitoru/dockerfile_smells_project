FROM frolvlad/alpine-glibc:alpine-3.4

ARG METRICBEAT_VERSION=5.1.1

ADD https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-${METRICBEAT_VERSION}-linux-x86_64.tar.gz /tmp/metricbeat.tar.gz
RUN tar -C /tmp -xzf /tmp/metricbeat.tar.gz \
 && mv /tmp/metricbeat-${METRICBEAT_VERSION}-linux-x86_64/ /usr/share/metricbeat/ \
 && true

ENTRYPOINT ["/usr/share/metricbeat/metricbeat"]
