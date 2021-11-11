FROM grafana/grafana:4.1.1

RUN apt-get update && apt-get install -y curl vim

ADD rootfs /

#/etc/resolv.conf 
# from docker_grafana
#nameserver 127.0.0.11
#options ndots:0



#RUN echo '# from docker_grafana\n\
#nameserver 127.0.0.11\n\
#options ndots:0' > /etc/resolv.conf && chmod 0444 /etc/resolv.conf
#CMD echo '# from docker_grafana\n\
#nameserver 127.0.0.11\n\
#options ndots:0' > /etc/resolv.conf && chmod 0444 /etc/resolv.conf


CMD sed 's/search telechargement.fr//' /etc/resolv.conf > /tmp/resolv.conf && cat /tmp/resolv.conf > /etc/resolv.conf


ARG "version=0.1.0-dev"
ARG "build_date=unknown"
ARG "commit_hash=unknown"
ARG "vcs_url=unknown"
ARG "vcs_branch=unknown"

LABEL org.label-schema.vendor="basi" \
    org.label-schema.name="Grafana" \
    org.label-schema.description="Grafana with some limited automated data sources creation" \
    org.label-schema.usage="/README.md" \
    org.label-schema.url="https://github.com/bvis/docker-grafana/blob/master/README.md" \
    org.label-schema.vcs-url=$vcs_url \
    org.label-schema.vcs-branch=$vcs_branch \
    org.label-schema.vcs-ref=$commit_hash \
    org.label-schema.version=$version \
    org.label-schema.schema-version="1.0" \
    org.label-schema.docker.cmd.devel="" \
    org.label-schema.docker.params="GF_SECURITY_ADMIN_PASSWORD=admin,\
PROMETHEUS_ENDPOINT=http://prometheus:9090,\
ELASTICSEARCH_ENDPOINT=http://elasticsearch:9200,\
ELASTICSEARCH_USER=readuser,\
ELASTICSEARCH_PASSWORD=myelasticpass" \
    org.label-schema.build-date=$build_date

ENV "IN=172.18.0.1:4999" \
    "OUT=4999"

ENV "GF_SECURITY_ADMIN_PASSWORD=admin" \
    "PROMETHEUS_ENDPOINT=http://prometheus:9090" \
    "ELASTICSEARCH_ENDPOINT=http://elasticsearch:9200" \
    "ELASTICSEARCH_USER=readuser" \
    "ELASTICSEARCH_PASSWORD=myelasticpass"


ENTRYPOINT ["/init.sh"]

