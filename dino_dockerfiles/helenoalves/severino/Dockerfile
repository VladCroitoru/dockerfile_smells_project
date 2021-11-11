
FROM jenkins/jenkins:alpine
MAINTAINER Heleno Alves <helenoa@gmail.com>

USER jenkins

COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/plugins.txt

USER root

ADD https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz /tmp
RUN tar -xvzf /tmp/docker-latest.tgz && \
    mv docker/* /usr/bin/ && \
    chmod +x /usr/bin/docker && \
    rm -f /tmp/docker-latest.tgz

RUN echo http://dl-2.alpinelinux.org/alpine/edge/community/ >> /etc/apk/repositories
RUN apk --no-cache add shadow nodejs
RUN apk -v --update add \
        python \
        py-pip \
        groff \
        less \
        mailcap \
        && \
    pip install --upgrade awscli s3cmd python-magic && \
    apk -v --purge del py-pip && \
    rm /var/cache/apk/*

RUN addgroup -g 933  docker
RUN addgroup jenkins docker
RUN usermod -aG docker jenkins