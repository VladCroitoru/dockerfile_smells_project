FROM ubuntu

ADD https://download.elastic.co/beats/filebeat/filebeat-1.3.0-x86_64.tar.gz /filebeat.tar.gz

RUN tar -xzf /filebeat.tar.gz && \
    rm -f /filebeat.tar.gz && \
    cp /filebeat-1.3.0-x86_64/filebeat /filebeat && \
    cp /filebeat-1.3.0-x86_64/filebeat.yml /filebeat.yml && \
    cp /filebeat-1.3.0-x86_64/filebeat.template.json /filebeat.template.json && \
    rm -Rf /filebeat-1.3.0-x86_64

CMD /filebeat

