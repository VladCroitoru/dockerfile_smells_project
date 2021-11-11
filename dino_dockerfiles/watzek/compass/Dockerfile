FROM ruby:2.4.1

# install nodejs runtime
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install -y nodejs

# install app
COPY . /usr/src/geoblacklight
WORKDIR /usr/src/geoblacklight
RUN bundle install

# configure app
ENV RAILS_ENV "production"
ENV RAILS_SERVE_STATIC_FILES "true"
ENV SOLR_URL "http://solr:8983/solr/compass"
ENV RABBIT_SERVER "amqp://mq:5672"

# persist data
VOLUME ["/usr/src/geoblacklight/tmp"]

# run
EXPOSE 3000
RUN rails assets:precompile
CMD ["rails", "s", "-b", "0.0.0.0"]
