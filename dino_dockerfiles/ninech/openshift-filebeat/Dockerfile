FROM debian:jessie

LABEL maintainer="nine.ch Engineering <engineering@nine.ch>"

ARG FILEBEAT_VERSION
ARG FILEBEAT_SHA
ARG FILEBEAT_SHA_TYPE

# update and install wget
# install and configure filebeat
# clean up
# If version is over 5.6.1 then we need to use a sha512 instead of 1
# copying the reference file can fail depending on version which is why it terminates with ; not &&
RUN set -x && \
    apt-get update && \
    apt-get install -y wget && \
    mkdir /filebeat /filebeat/config /filebeat/data && \
    chmod a+w /filebeat/data && \
    wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz -O /opt/filebeat.tar.gz && \
    cd /opt && \
    echo "${FILEBEAT_SHA}  filebeat.tar.gz" | ${FILEBEAT_SHA_TYPE}sum -c - && \
    tar xzvf filebeat.tar.gz && \
    cd filebeat-* && \
    cp filebeat /bin && \
    cp filebeat.template.json /filebeat ; \
    cp filebeat.reference.yml /filebeat ; \
    mv module /filebeat ; \
    cd /opt && \
    rm -rf filebeat* && \
    apt-get purge -y wget && \
    apt-get autoremove -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


WORKDIR /filebeat

# using a sample config file
COPY filebeat.yml ./config/
RUN chmod 0400 ./config/filebeat.yml

CMD [ "filebeat", "-e", "-path.config", "/filebeat/config", "-strict.perms=false" ]
