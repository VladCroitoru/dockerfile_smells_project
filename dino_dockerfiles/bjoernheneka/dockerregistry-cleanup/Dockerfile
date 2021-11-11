FROM registry:2

MAINTAINER Bjoern Heneka <bheneka@codebee.de>

RUN apt-get -qq update && \
    apt-get -y -q install python curl && \
    apt-get clean && \
    rm -fr /var/lib/apt/lists/*

RUN curl https://raw.githubusercontent.com/burnettk/delete-docker-registry-image/master/delete_docker_registry_image.py | \
    tee /usr/local/bin/delete_docker_registry_image >/dev/null && \
    chmod a+x /usr/local/bin/delete_docker_registry_image


RUN apt-get -y -q purge curl && \
    apt-get clean && \
    rm -fr /var/lib/apt/lists/*