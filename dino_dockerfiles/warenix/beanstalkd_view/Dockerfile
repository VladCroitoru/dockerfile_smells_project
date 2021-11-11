FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=2.0.0

RUN gem install beanstalkd_view --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["beanstalkd_view"]
CMD ["--help"]
