FROM malet/blueocean
USER root
RUN DEBIAN_FRONTEND=noninteractive \
  apt-get update && \
  apt-get purge docker.io* && \
  apt-get install -y -q \
    apt-transport-https \
    ca-certificates && \
  apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

RUN DEBIAN_FRONTEND=noninteractive \
  echo 'deb https://apt.dockerproject.org/repo debian-jessie main' >> \
    /etc/apt/sources.list.d/docker.list && \
  apt-cache policy docker-engine && \
  apt-get update && \
  apt-get install -y -q docker-engine && \
  gpasswd -a jenkins docker

COPY jenkins-docker.sh /usr/local/bin/jenkins-docker.sh

ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins-docker.sh"]
