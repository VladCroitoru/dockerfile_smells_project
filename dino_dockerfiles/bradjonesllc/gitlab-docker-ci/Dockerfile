FROM gitlab/gitlab-runner:v9.0.0

RUN apt-get update && apt-get install -yqq --no-install-recommends \
    curl \
    php5-cli \
    && apt-get clean autoclean && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

ENV DOCKER_VERSION 17.03.1-ce
RUN curl -fsSL \
    "https://get.docker.com/builds/$(uname -s)/$(uname -m)/docker-${DOCKER_VERSION}.tgz" | tar xz > docker \
    && mv docker/docker /usr/local/bin/docker \
    && rm -rf docker

# Install docker-compose
ENV DOCKER_COMPOSE_VERSION 1.11.2
RUN curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" > /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

# Install composer.
RUN php -r "readfile('https://getcomposer.org/installer');" | php && mv composer.phar /usr/local/bin/composer

COPY *.sh /
ENTRYPOINT /bootstrap.sh
