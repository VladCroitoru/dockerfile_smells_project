# Pull base image.
FROM centos:centos7

# update & base packages
RUN \
  yum update -y && \
  yum groupinstall -y "Development Tools" && \
  yum install -y curl tar java-1.7.0-openjdk && \
  yum clean all

# install jruby
RUN curl -L https://s3.amazonaws.com/jruby.org/downloads/1.7.21/jruby-bin-1.7.21.tar.gz | tar zxf -
RUN mkdir -p /usr/lib/jruby && mv jruby-1.7.21 /usr/lib/jruby
ENV PATH /usr/lib/jruby/jruby-1.7.21/bin:$PATH

# install norikra
RUN gem install norikra --no-ri --no-rdoc
RUN mkdir -p /var/log/norikra

# run norikra
EXPOSE 26571 26578
CMD norikra start -Xmx2g --pidfile /var/run/norikra.pid --logdir=/var/log/norikra

