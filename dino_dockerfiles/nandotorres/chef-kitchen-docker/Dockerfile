FROM ruby:2.3.1

MAINTAINER "ftorres@avenuecode.com"

RUN mkdir -p /usr/src/app

RUN wget -qO- https://get.docker.com/ | sh && \
    wget https://packages.chef.io/stable/ubuntu/12.04/chefdk_0.19.6-1_amd64.deb && \
    dpkg -i chefdk_0.19.6-1_amd64.deb && \
    /opt/chefdk/bin/chef gem install specific_install && \
    /opt/chefdk/bin/chef gem specific_install kitchen-docker -l http://github.com/peterabbott/kitchen-docker.git -b v2.6.0

WORKDIR  /usr/src/app

ENTRYPOINT ["/opt/chefdk/bin/chef", "exec"]
