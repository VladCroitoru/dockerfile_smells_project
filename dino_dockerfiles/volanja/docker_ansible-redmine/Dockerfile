FROM centos:centos6

MAINTAINER volanja "https://github.com/volanja"

ENV RUBY_VERSION 2.3.3

### Packages
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm \
&& yum update -y \
&& yum install -y ansible \
&& yum install -y passwd openssh openssh-server openssh-clients initscripts sudo \
&& yum install -y vim git-all

### SSHD
RUN sed -ri 's/#PermitRootLogin yes/PermitRootLogin yes/g' /etc/ssh/sshd_config \
&& sed -ri 's/^PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config \
&& sed -ri 's/^#UsePAM yes/UsePAM yes/g' /etc/ssh/sshd_config

## Ruby
RUN yum groupinstall -y "Development tools" \
&& yum install -y tar libffi-devel openssl openssl-devel readline-devel readline compat-readline5 libxml2-devel libxslt-devel libyaml-devel git ImageMagick ImageMagick-devel ipa-pgothic-fonts

### Install Ruby
RUN curl -O http://ftp.ruby-lang.org/pub/ruby/ruby-$RUBY_VERSION.tar.gz \
&& tar zvxf ruby-$RUBY_VERSION.tar.gz \
&& pushd ruby-$RUBY_VERSION \
&& ./configure && make && make install \
&& popd \
&& rm -rf ruby-$RUBY_VERSION.tar.gz ruby-$RUBY_VERSION


### Install bundler
RUN gem update --system \
&& gem install bundler serverspec infrataster ansible_spec --no-rdoc --no-ri

RUN service sshd start

## iptables
RUN echo 'IPTABLES_MODULES_UNLOAD=no' >> /etc/sysconfig/iptables-config
COPY src/iptables /etc/sysconfig/iptables

EXPOSE 22

CMD /sbin/init
