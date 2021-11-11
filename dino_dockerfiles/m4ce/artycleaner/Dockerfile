FROM centos:7
MAINTAINER Matteo Cerutti <matteo.cerutti@hotmail.co.uk>

ADD Gemfile /app/

RUN yum clean all && \
    yum install -y epel-release centos-release-scl && \
    yum install -y make gcc-c++ rh-ruby22-ruby-devel rh-ruby22-rubygem-bundler && \
    cd /app && \
    scl enable rh-ruby22 -- bundle install && \
    rm -rf /var/cache/yum/*

ADD artycleaner.rb /app/
ADD artycleaner.yaml /app/

WORKDIR "/app"
ENTRYPOINT ["/usr/bin/scl", "enable", "rh-ruby22", "--", "/app/artycleaner.rb"]
