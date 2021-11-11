FROM registry.access.redhat.com/ubi8/ruby-27
MAINTAINER Eguzki Astiz Lezaun <eastizle@redhat.com>

USER root
WORKDIR /usr/src/app
COPY . .
RUN gem build 3scale_toolbox.gemspec
RUN gem install 3scale_toolbox-*.gem --no-document

# clean up
RUN rm -rf /usr/src/app

# Drop privileges
USER default
WORKDIR /opt/app-root/src

CMD ["/bin/bash"]
