FROM gcr.io/google_containers/kibana:v4.6.1

RUN /kibana/bin/kibana plugin -i logtrail -u https://github.com/sivasamyk/logtrail/releases/download/0.1.7/logtrail-4.x-0.1.7.tar.gz

COPY logtrail.json /kibana/installedPlugins/logtrail/logtrail.json
