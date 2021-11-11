FROM factual/docker-base

MAINTAINER agate<agate.hao@gmail.com>

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y curl
RUN apt-get install -y build-essential

RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
RUN \curl -sSL https://get.rvm.io | bash -s stable
RUN bash -l -c "rvm requirements"

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD bootstrap.sh /etc/my_init.d/099_bootstrap
