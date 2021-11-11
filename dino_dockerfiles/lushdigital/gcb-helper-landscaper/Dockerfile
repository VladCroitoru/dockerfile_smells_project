FROM google/cloud-sdk

MAINTAINER Simon Ince <simon.ince@lush.co.uk>

ENV VERSION v2.2.2
ENV FILENAME helm-${VERSION}-linux-amd64.tar.gz

WORKDIR /

ADD https://storage.googleapis.com/kubernetes-helm/${FILENAME} /tmp

COPY helm_install_or_upgrade /bin/
COPY landscaper /bin/

RUN tar -zxvf /tmp/${FILENAME} -C /tmp \
  && mv /tmp/linux-amd64/helm /bin/helm \
  && rm -rf /tmp

RUN helm init --client-only

RUN helm repo add soa-chart-repository https://soa-chart-repository.storage.googleapis.com
