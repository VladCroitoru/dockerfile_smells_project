FROM jenkins/jenkins

USER root

ENV DOCKER_COMPOSE_VERSION=1.15.0

RUN apt-get update \
    && apt-get install -y \
       apt-transport-https \
       ca-certificates \
       curl \
       gnupg2 \
       software-properties-common \
   && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - >/dev/null \
    && apt-key fingerprint 0EBFCD88 | grep "9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88"

RUN groupadd -g 998 docker

RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
    && apt-get update \
    && apt-get install -y \
       docker-ce \
       jq \
    && rm -rf /var/lib/apt/lists/* \
    && curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose \
    && usermod -a -G docker jenkins \
    && systemctl enable docker

ENV SIGIL_URL https://github.com/gliderlabs/sigil/releases/download/v0.4.0/sigil_0.4.0_Linux_x86_64.tgz

RUN set -ex \
    && wget -q $SIGIL_URL -O sigil.tgz \
    && tar -zxv -C /usr/local/bin -f sigil.tgz \
    && rm sigil.tgz

USER jenkins
