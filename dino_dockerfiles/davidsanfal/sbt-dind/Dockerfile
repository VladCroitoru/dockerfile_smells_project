FROM ubuntu:16.04

RUN apt-get update -qq && \
    apt-get upgrade -y && \
    apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    curl \
    lxc \
    iptables && \
    curl -sSL https://get.docker.com/ | sh && \
    apt-get install -y --fix-missing docker-engine \
    software-properties-common \
    apt-transport-https \
    python3 \
    python3-pip \
    libyaml-dev && \
    add-apt-repository ppa:openjdk-r/ppa && \
    apt-get install -y openjdk-8-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -L -o sbt.deb http://dl.bintray.com/sbt/debian/sbt-0.13.13.deb && \
    dpkg -i sbt.deb

RUN curl -L https://github.com/docker/compose/releases/download/1.13.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

RUN sbt about
RUN docker-compose version

COPY start.sh /
RUN chmod +x /start.sh
ENTRYPOINT ["/bin/sh", "/start.sh"]
