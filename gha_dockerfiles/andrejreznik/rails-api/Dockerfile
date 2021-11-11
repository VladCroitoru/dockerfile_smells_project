FROM ruby:3.0.2

LABEL maintainer="Andrii Rieznik <andrii.rieznik@pm.com>"

COPY Gemfile Gemfile.lock ./

RUN bundle install

WORKDIR /workspace

CMD [ "/bin/bash" ]
