FROM ruby:3.0-alpine as Builder
RUN apk --update add g++ make musl-dev

WORKDIR /app

COPY ./src/Gemfile ./src/Gemfile.lock  ./
RUN bundle config --global frozen 1 \
 && bundle install --without development test -j4 --retry 3 \
 # Remove unneeded files (cached *.gem, *.o, *.c)
 && rm -rf /usr/local/bundle/cache/*.gem \
 && find /usr/local/bundle/gems/ -name "*.c" -delete \
 && find /usr/local/bundle/gems/ -name "*.o" -delete

COPY ./src .

FROM ruby:3.0-alpine
RUN apk --update add nodejs tzdata

COPY --from=Builder /usr/local/bundle /usr/local/bundle
COPY --from=Builder /app /app

ENV TRAFFIC_HOST feedback.chaosdorf.space
ENV MOSQUITTO_HOST mqttserver.chaosdorf.space
ENV PING_HOST speedtest-2.unitymedia.de

WORKDIR /app

# Define environment variable
ENV RACK_ENV production

ENTRYPOINT ["bundle", "exec", "smashing", "start"]

EXPOSE 3030/tcp
