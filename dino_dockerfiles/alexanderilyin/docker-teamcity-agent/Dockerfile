FROM java

MAINTAINER Alexander Ilyin <ailyin@anchorfree.com>

# INSTALL TEAMCITY BUILD AGENT
RUN mkdir -v /opt/buildAgent \
    && cd /opt/buildAgent \
    && curl -LSs https://teamcity.jetbrains.com/update/buildAgent.zip | jar xvf /dev/stdin \
    && chmod -c +x /opt/buildAgent/bin/agent.sh

# INSTALL DOCKER
RUN apt-get update \
    && apt-get install --yes apt-transport-https ca-certificates \
    && apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
    && echo 'deb https://apt.dockerproject.org/repo debian-jessie main' > /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get install --yes docker-engine \
    && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /entrypoint.sh

VOLUME [ "/opt/buildAgent/work", "/opt/buildAgent/logs"]

ENTRYPOINT ["/entrypoint.sh"]
