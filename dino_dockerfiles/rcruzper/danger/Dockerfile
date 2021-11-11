FROM ruby:2.3.1

RUN gem install danger && \
    gem install danger-commit_lint && \
    gem install danger-prose

ENTRYPOINT danger
