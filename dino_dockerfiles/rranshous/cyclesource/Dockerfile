FROM ruby:2.2.0

RUN mkdir /data
VOLUME /data

ADD . /app
WORKDIR /app
RUN bundle install --without development --without test --without client

VOLUME /var/run/docker.sock

EXPOSE 80
ENV PORT=80
ENV HOST=0.0.0.0
ENV DATA_DIR=/data

ENTRYPOINT ["bundle", "exec"]
CMD ["ruby", "app.rb"]
