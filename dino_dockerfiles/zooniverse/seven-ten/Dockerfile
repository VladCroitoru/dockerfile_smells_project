FROM ruby:2.6-stretch

ARG RAILS_ENV
ARG REVISION=''
ENV REVISION=$REVISION

WORKDIR /rails_app

RUN apt-get update && \
  apt-get install --no-install-recommends -y libpq-dev && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./Gemfile /rails_app/
COPY ./Gemfile.lock /rails_app/

RUN cd /rails_app && \
  bundle install --without test development

COPY ./ /rails_app

ENV RAILS_ENV $RAILS_ENV
ENV RACK_ENV $RAILS_ENV

EXPOSE 80

CMD ["/rails_app/docker/start.sh"]
