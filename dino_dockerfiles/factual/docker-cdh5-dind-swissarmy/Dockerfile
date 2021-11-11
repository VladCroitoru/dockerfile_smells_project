FROM factual/docker-cdh5-base

ENV DOCKER_CHANNEL=stable \
    DOCKER_VERSION=17.12.0

VOLUME /var/lib/docker

RUN echo "== Add docker source =>" && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) \
      $DOCKER_CHANNEL" && \
    \
    echo "== Install apt packages =>" && \
    apt-get update && \
    apt-get install -y \
      sudo \
      git-core \
      docker-ce=`apt-cache madison docker-ce | grep $DOCKER_VERSION | awk '{ print $3 }'` \
      && \
    \
    echo "== Cleanup =>" && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD bootstrap.sh /etc/my_init.d/099_bootstrap
