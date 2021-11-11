FROM wingrunr21/drone-base
MAINTAINER Stafford Brunk <stafford.brunk@gmail.com>

ENV SHELL /bin/bash
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

RUN apt-get update

RUN ruby-install ruby  1.9.3-p551
RUN ruby-install ruby  2.0.0-p645
RUN ruby-install ruby  2.1.6
RUN ruby-install ruby  2.2.2
RUN ruby-install jruby 1.7.21
RUN ruby-install jruby 9.0.0.0
RUN ruby-install rbx 2.5.8

RUN /bin/bash -l -c "chruby 1.9.3 && gem install bundler --no-rdoc --no-ri"
RUN /bin/bash -l -c "chruby 2.0.0 && gem install bundler --no-rdoc --no-ri"
RUN /bin/bash -l -c "chruby 2.1.6 && gem install bundler --no-rdoc --no-ri"
RUN /bin/bash -l -c "chruby 2.2.2 && gem install bundler --no-rdoc --no-ri"
RUN /bin/bash -l -c "chruby jruby-1.7.21 && gem install bundler --no-rdoc --no-ri"
RUN /bin/bash -l -c "chruby jruby-9.0.0.0 && gem install bundler --no-rdoc --no-ri"
RUN /bin/bash -l -c "chruby rbx-2.5.8 && gem install bundler --no-rdoc --no-ri"
