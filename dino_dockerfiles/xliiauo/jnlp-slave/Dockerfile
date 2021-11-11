FROM jenkinsci/jnlp-slave:3.23-1

USER root

RUN curl -O https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz &&\
    tar -xvzf docker-latest.tgz &&\
    mv docker/docker /usr/bin/docker &&\
    rm -rf docker/ docker-latest.tgz
