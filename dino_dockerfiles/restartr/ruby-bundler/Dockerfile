FROM centos:6

ENV RUBY_MAJOR   2.0
ENV RUBY_VERSION 2.0.0-p481

RUN yum -y -q install wget tar gcc \
      byacc readline-devel ncourses-devel tcl-devel openssl-devel gdbm-devel db4-devel

WORKDIR /

ADD . /tmp
RUN bash /tmp/install-ruby.sh

RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc" && \
    gem install bundler

VOLUME /app
VOLUME /opt/app/vendor

WORKDIR /app
CMD [ "bash", "startup.sh" ]
