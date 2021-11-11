FROM centos:7
MAINTAINER Krzysztof Treyderowski <krzysztof.treyderowski@lhsystems.com>
RUN rpm -ivh https://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm
RUN yum -y install puppet
RUN gem install puppet-lint
RUN echo testing automatic build
