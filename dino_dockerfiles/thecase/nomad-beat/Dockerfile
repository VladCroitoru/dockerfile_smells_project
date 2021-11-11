FROM alpine:3.5

RUN apk update && apk add supervisor ca-certificates wget tar && update-ca-certificates
# needed for metricbeat
RUN wget "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.21-r2/glibc-2.21-r2.apk" \
         "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.21-r2/glibc-bin-2.21-r2.apk" && \
         apk add --allow-untrusted glibc-2.21-r2.apk glibc-bin-2.21-r2.apk && \
         /usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib && \
        rm -rf *.apk
        
ENV DOCKERGEN_VERSION=0.7.3
RUN wget https://github.com/jwilder/docker-gen/releases/download/${DOCKERGEN_VERSION}/docker-gen-linux-amd64-${DOCKERGEN_VERSION}.tar.gz -O- | \
    tar xvz -C /usr/local/bin/ docker-gen

ENV FILEBEAT_VERSION=6.2.1
RUN wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz -O- | \
    tar xvz -C /usr/local/bin/ --strip-components 1 filebeat-${FILEBEAT_VERSION}-linux-x86_64/filebeat

ENV METRICBEAT_VERSION=6.2.1
RUN wget https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-${METRICBEAT_VERSION}-linux-x86_64.tar.gz -O- | \
    tar xvz -C /usr/local/bin/ --strip-components 1 metricbeat-${METRICBEAT_VERSION}-linux-x86_64/metricbeat

#ENV LOGSTASH_HOST=filebeat.domain.com:443
#ADD certs/logstash-forwarder.crt /etc/pki/tls/certs/logstash-forwarder.crt
#ADD certs/logstash-forwarder.key /etc/pki/tls/private/logstash-forwarder.key

ADD supervisord.conf /etc/supervisord.conf
ADD filebeat.tmpl /etc/docker-gen/filebeat.tmpl
ADD metricbeat.yml /etc/beats/metricbeat.yml
RUN chmod go-w /etc/beats/metricbeat.yml

CMD ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]

