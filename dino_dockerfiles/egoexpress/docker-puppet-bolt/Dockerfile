FROM ruby:2.5

ARG bolt_version=0.19.0

LABEL maintainer="bjoern-github@innovention.de"

RUN gem install bolt -v ${bolt_version}

RUN groupadd -r bolt && useradd --no-log-init -r -g bolt bolt

USER bolt:bolt
ENTRYPOINT ["bolt"]
CMD ["--help"]
