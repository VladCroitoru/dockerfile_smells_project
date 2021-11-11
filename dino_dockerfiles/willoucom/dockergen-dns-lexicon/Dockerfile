FROM ubuntu:16.04
MAINTAINER Wilfried JEANNIARD <willou.com@gmail.com>

# Install packages
RUN apt-get update \
  && apt-get install -y wget python-pip \
  && apt-get clean &&  rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
  && pip install boto3 dns-lexicon dns-lexicon[route53] supervisor

# Install docker-gen
ENV DOCKER_GEN_VERSION 0.7.3
RUN wget https://github.com/jwilder/docker-gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \
 && tar -C /usr/local/bin -xvzf docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \
 && rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz

# Install app
COPY files /

ENV DOCKER_HOST unix:///tmp/docker.sock

ENTRYPOINT ["bash","/app/docker-entrypoint.sh"]
CMD ["supervisord", "-c","/etc/supervisord.conf"]
