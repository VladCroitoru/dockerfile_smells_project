FROM ubuntu:12.04
MAINTAINER Gabriel Glachant <gglachant@gmail.com>

ENV RUBY ruby
ENV RUBY_VERSION 2.0.0-p481

ENV DEBIAN_FRONTEND noninteractive

#RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get -qy update && apt-get -qy install apt-utils ca-certificates curl git-core sudo && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

RUN locale-gen  en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN bash -l -c "if [ ! -h /dev/fd ]; then ln -s /proc/self/fd /dev/fd; fi && curl -sL https://get.rvm.io | bash -s stable"
RUN bash -l -c "if [ ! -h /dev/fd ]; then ln -s /proc/self/fd /dev/fd; fi && source /etc/profile.d/rvm.sh && /usr/local/rvm/bin/rvm requirements"
RUN bash -l -c "if [ ! -h /dev/fd ]; then ln -s /proc/self/fd /dev/fd; fi && source /etc/profile.d/rvm.sh && rvm install $RUBY-$RUBY_VERSION --binary --autolibs=enabled"
RUN bash -l -c "if [ ! -h /dev/fd ]; then ln -s /proc/self/fd /dev/fd; fi && source /etc/profile.d/rvm.sh && rvm use ${RUBY}-${RUBY_VERSION}"
RUN echo "source /etc/profile.d/rvm.sh" >> /etc/profile
RUN echo "rvm --default use $RUBY-$RUBY_VERSION" >> /etc/profile
RUN bash -l -c "if [ ! -h /dev/fd ]; then ln -s /proc/self/fd /dev/fd; fi && source /etc/profile.d/rvm.sh && rvm alias create default $RUBY_VERSION"
RUN bash -l -c "if [ ! -h /dev/fd ]; then ln -s /proc/self/fd /dev/fd; fi && source /etc/profile.d/rvm.sh && rvm ${RUBY}-${RUBY_VERSION} do gem install bundler --no-ri --no-rdoc"

ENTRYPOINT ["/bin/bash"]
