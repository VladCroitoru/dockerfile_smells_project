FROM ubuntu:12.04

RUN apt-get update
RUN apt-get install -y curl sudo

RUN curl -sSL https://get.rvm.io | bash -s master
RUN /usr/local/rvm/bin/rvm install 2.0.0-p647
RUN curl -LO https://www.chef.io/chef/install.sh && sudo bash ./install.sh -v 11.10.0
RUN export PATH=$PATH:/usr/local/rvm/rubies/ruby-2.0.0-p647/bin && gem install chef -v 11.10.0

RUN ln -s /usr/local/rvm/rubies/ruby-2.0.0-p647/bin/ruby /usr/bin/ruby

RUN rm -rf /opt/chef/embedded/bin
RUN ln -s /usr/local/rvm/rubies/ruby-2.0.0-p647/bin /opt/chef/embedded/bin

RUN rm -rf /opt/chef/embedded/include/ruby-1.9.1
RUN ln -s /usr/local/rvm/rubies/ruby-2.0.0-p647/include/ruby-2.0.0 /opt/chef/embedded/include/ruby-1.9.1

RUN rm -rf /opt/chef/embedded/lib/ruby/1.9.1
RUN ln -s /usr/local/rvm/rubies/ruby-2.0.0-p647/lib/ruby/2.0.0 /opt/chef/embedded/lib/ruby/1.9.1

RUN rm -rf /opt/chef/embedded/lib/ruby/site_ruby/1.9.1
RUN ln -s /usr/local/rvm/rubies/ruby-2.0.0-p647/lib/ruby/site_ruby/2.0.0 /opt/chef/embedded/lib/ruby/site_ruby/1.9.1

RUN rm -rf /opt/chef/embedded/lib/ruby/vendor_ruby/1.9.1
RUN ln -s /usr/local/rvm/rubies/ruby-2.0.0-p647/lib/ruby/vendor_ruby/2.0.0 /opt/chef/embedded/lib/ruby/vendor_ruby/1.9.1

RUN rm -rf /opt/chef/embedded/lib/ruby/gems/1.9.1
RUN ln -s /usr/local/rvm/rubies/ruby-2.0.0-p647/lib/ruby/gems/2.0.0 /opt/chef/embedded/lib/ruby/gems/1.9.1
