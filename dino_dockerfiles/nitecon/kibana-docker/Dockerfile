FROM docker.elastic.co/kibana/kibana:6.1.3

ADD kibana.yml /usr/share/kibana/config/kibana.yml
RUN bin/kibana-plugin remove x-pack && \
    timeout 120s /usr/share/kibana/bin/kibana || true
VOLUME [ "/data" ]