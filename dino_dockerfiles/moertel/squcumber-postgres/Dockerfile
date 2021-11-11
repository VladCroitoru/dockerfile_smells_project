FROM ruby:2.3.0 as builder
COPY ./lib lib
COPY ./spec spec
COPY ./Rakefile .
COPY ./Gemfile .
COPY ./squcumber-postgres.gemspec .
RUN gem build squcumber-postgres.gemspec

FROM ruby:2.3.0
ENV CUSTOM_STEPS_DIR /custom_step_definitions
VOLUME /custom_step_definitions
VOLUME /features
VOLUME /sql
COPY --from=builder /squcumber-postgres*.gem squcumber-postgres.gem
RUN gem install ./squcumber-postgres.gem
RUN echo "require 'squcumber-postgres/rake/task'" > Rakefile

ENTRYPOINT ["rake"]
CMD ["test:sql:features"]
