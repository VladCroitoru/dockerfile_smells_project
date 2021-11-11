FROM ruby:2.2

ADD ./ /app
WORKDIR /app
RUN bundle install

EXPOSE 80
VOLUME /data

ENV HTTP_PORT 80
ENV STATE_DIR /data

ENTRYPOINT ["bundle", "exec", "ruby"]
CMD ["event_type_tracker.rb"]
