FROM quay.io/evryfs/base-ubuntu:focal-20211006
LABEL maintainer "fsdevops@evry.com"
ARG OEC_VERSION=1.1.3
RUN curl -L https://github.com/opsgenie/oec/releases/download/${OEC_VERSION}/oec-linux-amd64-${OEC_VERSION}.zip -o /tmp/oec.zip && unzip /tmp/oec.zip && rm /tmp/oec.zip && \
  apt-get update && apt-get -y --no-install-recommends install groovy && apt-get clean && rm -rf /var/cache/apt
ENTRYPOINT ["/OpsgenieEdgeConnector"]
