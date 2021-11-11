FROM ubuntu-debootstrap:14.04
MAINTAINER Raphael Valyi <rvalyi@akretion.com>

RUN apt-get update
RUN apt-get install curl git -y

RUN curl -L https://www.opscode.com/chef/install.sh | bash -s -- -P chefdk
RUN locale-gen en_US.UTF-8

ADD Gemfile /Gemfile
ADD .kitchen.sample.yml /.kitchen.sample.yml
RUN /opt/chefdk/embedded/bin/bundle install
RUN echo "gem 'berkshelf', '>= 3.0.0'" >> Gemfile

RUN curl -k https://dl.gliderlabs.com/sigil/latest/$(uname -sm|tr \  _).tgz | tar -zxC /usr/local/bin

WORKDIR /workspace
ADD bundle_exec_wrapper /bundle_exec_wrapper
ADD user.tmpl /user.tmpl
ADD Berksfile.sample /Berksfile.sample
ENTRYPOINT ["/bundle_exec_wrapper"]
