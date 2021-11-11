FROM buildpack-deps:jessie-curl

ENV RANCHER_CLI_VERSION 0.1.0
ENV RANCHER_CLI_HOME /usr/lib/rancher-cli

RUN apt-get update \
  && apt-get install -y apt-transport-https ca-certificates \
  && echo "deb https://apt.dockerproject.org/repo debian-jessie main" > /etc/apt/sources.list.d/docker.list \
  && apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
  && apt-get update -y \
  && apt-get install -y docker-engine

ADD install-tools.sh /usr/local/bin/

RUN mkdir ${RANCHER_CLI_HOME} && /usr/local/bin/install-tools.sh

VOLUME ${RANCHER_CLI_HOME}

ENTRYPOINT ["/usr/lib/rancher-cli/rancher"]
CMD ["--version"]
