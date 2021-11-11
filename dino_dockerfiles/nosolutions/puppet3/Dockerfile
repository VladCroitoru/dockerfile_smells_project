FROM centos:7.3.1611
MAINTAINER Toni Schmidbauer <toni@stderr.at>

ARG http_proxy

ENV http_proxy  ${http_proxy}
ENV https_proxy ${http_proxy}

COPY puppetlabs-release-el-7.noarch.rpm /tmp/
COPY gitlab-runner.repo /etc/yum.repos.d/gitlab-runner.repo
COPY Gemfile /tmp/

WORKDIR /workspace

RUN yum -y -q localinstall /tmp/puppetlabs-release-el-7.noarch.rpm \
 && yum -y -q install puppet ruby-devel make gcc git \
 && yum clean all \
 && gem install --no-ri --no-rdoc bundler \
 && bundle install --system --gemfile /tmp/Gemfile \
 && useradd -u 1000 vagrant

USER vagrant
