# https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-docker.html
FROM amazon/aws-cli:2.0.6

RUN yum -y install tar
RUN yum -y install gzip
RUN yum -y install git
RUN yum -y install curl
RUN yum -y install which

ENV VERSION v3.2.4
ENV FILENAME helm-${VERSION}-linux-amd64.tar.gz

WORKDIR /

ADD https://get.helm.sh/${FILENAME} /tmp

RUN tar -zxvf /tmp/${FILENAME} -C /tmp \
  && mv /tmp/linux-amd64/helm /bin/helm 

COPY deploy.sh /bin/deploy.sh
RUN chmod +x /bin/deploy.sh
ENTRYPOINT ["/bin/deploy.sh"]
