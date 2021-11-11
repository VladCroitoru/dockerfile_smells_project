FROM ubuntu:14.04
MAINTAINER Huttopia <dev@huttopia.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq
RUN apt-get install -qqy software-properties-common python-software-properties
RUN add-apt-repository -y ppa:git-core/ppa && \
    add-apt-repository -y ppa:brightbox/ruby-ng && \
    apt-get update -qq && \
    apt-get install -qqy build-essential checkinstall \
      git-core zlib1g-dev libyaml-dev libssl-dev \
      libgdbm-dev libreadline-dev libncurses5-dev libffi-dev \
      libxml2-dev libxslt-dev libcurl4-openssl-dev libicu-dev \
      ruby2.1 ruby2.1-dev openssh-client && \
    gem install --no-ri --no-rdoc bundler && \
    rm -rf /var/lib/apt/lists/* # 20140818

# Installe les certificats LXC
RUN apt-get update -qq
RUN apt-get install -qqy iptables ca-certificates lxc

# Installation de docker LXC
RUN apt-get install -qqy apt-transport-https
RUN echo deb https://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
RUN apt-get update -qq
RUN apt-get install -qqy lxc-docker

# Installation de curl
RUN apt-get install -qqy curl

# Fig
RUN curl -L https://github.com/docker/fig/releases/download/1.0.1/fig-`uname -s`-`uname -m` > /usr/local/bin/fig; chmod +x /usr/local/bin/fig

# Java
RUN apt-get update -qq && apt-get install -qqy default-jre

# Droits sudo sans password pour gitlab_ci_runner
RUN chmod 755 /etc/sudoers
RUN echo "gitlab_ci_runner ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

ADD assets/setup/ /app/setup/
RUN chmod 755 /app/setup/install
RUN /app/setup/install

ADD assets/init /app/init
RUN chmod 755 /app/init

VOLUME ["/home/gitlab_ci_runner/data"]

# Chargement du docker du host pour lancer du docker dans ce docker
VOLUME /var/lib/docker

ENTRYPOINT ["/app/init"]
CMD ["app:start"]
