FROM ruby:2.6.5
# copy application code
COPY Gemfile /terraling/Gemfile
COPY Gemfile.lock /terraling/Gemfile.lock
# change working directory
WORKDIR /terraling

ENV RAILS_ENV production

# 2.1.4 is required
RUN gem install bundler:2.1.4
RUN bundle install

RUN apt-get update && apt-get -y install nodejs

ENTRYPOINT ["/terraling/docker-entry.sh"]
CMD ["run"]
