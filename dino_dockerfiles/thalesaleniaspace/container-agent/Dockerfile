FROM centos

ADD https://github.com/openfaas/faas/releases/download/0.7.1/fwatchdog /usr/bin
RUN chmod +x /usr/bin/fwatchdog
RUN yum install -y yum-utils device-mapper-persistent-data lvm2 &&\
    yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo &&\
    yum install -y docker-ce &&\
    yum install -y net-tools iproute && yum clean all

ADD resources/docker-run.sh /opt/docker-run.sh

CMD chmod +x /opt/docker-run.sh
HEALTHCHECK --interval=5s CMD [ -e /tmp/.lock ] || exit 1

LABEL com.openfaas.scale.min="3"
LABEL com.openfaas.scale.max="3"

CMD ["fwatchdog"]
