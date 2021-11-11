FROM jenkins/jenkins

ENV docker_ver=19.03.9
ENV ansible_ver=2.8

USER root:root

RUN wget https://download.docker.com/linux/static/stable/x86_64/docker-${docker_ver}.tgz \
    && tar -xvf docker-${docker_ver}.tgz \
    && mv docker/docker /usr/bin/docker \
    && rm -rf docker

RUN apt-get update \
    && apt-get dist-upgrade -y \
    && apt-get install -y software-properties-common ca-certificates apt-transport-https

RUN wget -q https://packages.sury.org/php/apt.gpg -O- | apt-key add - \
    && echo "deb https://packages.sury.org/php/ stretch main" > /etc/apt/sources.list.d/php.list \
    && apt-get update \
    && apt-get install -y python3-pip sshpass php5.6 php5.6-mysql mysql-utilities mysql-client \
    && apt-get clean

RUN pip3 install docker-py ansible==${ansible_ver}.*
