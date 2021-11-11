FROM jenkins/jenkins:lts
LABEL maintainer="herve.leclerc@alterway.fr"
ENV DOCKERVERSION=18.03.0-ce
ENV COMPOSEVERSION=1.21.0
# needed to install software demo
USER root
RUN apt-get update \
    && apt-get install -y python-pip \
    && pip install awscli --upgrade \
    && curl -fsSLO https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKERVERSION}.tgz \
    && mv docker-${DOCKERVERSION}.tgz docker.tgz \
    && tar xzvf docker.tgz \
    && mv docker/docker /usr/local/bin \
    && rm -rf docker docker.tgz \
    && curl -fsSL https://github.com/docker/compose/releases/download/${COMPOSEVERSION}/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose \
    && chmod a+rx /usr/local/bin/docker-compose
