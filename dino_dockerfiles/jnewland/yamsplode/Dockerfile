FROM ruby:2.5-slim-stretch
WORKDIR /usr/src/app
COPY Gemfile* /usr/src/app/
RUN bundle install
COPY *.rb /usr/src/app/
ENTRYPOINT ["bundle", "exec", "ruby", "/usr/src/app/yamsplode.rb"]
CMD ["/in.yaml", "/out"]
