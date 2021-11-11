FROM centos:centos6

MAINTAINER volanja "https://github.com/volanja/docker-ansible"

ENV RUBY_VERSION 2.3.0

### Packages
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN yum update -y
RUN yum install -y ansible
RUN yum install -y openssh-clients initscripts

RUN yum groupinstall -y "Development tools"
RUN yum install -y tar libffi-devel openssl openssl-devel readline-devel readline compat-readline5 libxml2-devel libxslt-devel libyaml-devel git

### Install Ruby
RUN curl -O http://ftp.ruby-lang.org/pub/ruby/ruby-$RUBY_VERSION.tar.gz && tar zvxf ruby-$RUBY_VERSION.tar.gz && pushd ruby-$RUBY_VERSION && ./configure && make && make install && popd && rm -rf ruby-$RUBY_VERSION.tar.gz ruby-$RUBY_VERSION

### Install bundler
RUN gem update --system
RUN gem install bundler serverspec infrataster ansible_spec --no-rdoc --no-ri

EXPOSE 22

CMD /sbin/init
