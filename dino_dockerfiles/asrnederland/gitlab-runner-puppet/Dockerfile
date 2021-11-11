FROM centos:7
MAINTAINER Nick Hilhorst <nick.hilhorst@asr.nl>

ENV PATH="/opt/puppetlabs/puppet/bin:${PATH}"
RUN yum install -y https://yum.puppetlabs.com/puppet5/puppet5-release-el-7.noarch.rpm && \
    yum update -y && \
    yum install -y \
        gcc \
        make \
        ruby \
        ruby-devel \
        zlib-devel \
        libxslt-devel \
        libxml2-devel \
        puppet-agent-5.5.17-1.el7 \
        git && \
    yum clean all

RUN gem install actionpack:4.2.11.1 activesupport:4.2.11.1 --no-ri --no-rdoc

RUN gem install --minimal-deps --no-ri --no-rdoc \
        yaml-lint \
        puppet-lint \
        rails-erb-check \
        rails-erb-lint \
        ruby-lint \
        rspec-puppet \
        puppetlabs_spec_helper
