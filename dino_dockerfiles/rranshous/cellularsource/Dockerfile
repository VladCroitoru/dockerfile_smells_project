FROM ruby:2.2.0

ADD . /app
WORKDIR /app
RUN bundle install --without development --without test

EXPOSE 80
ENV PORT=80
ENV HOST=0.0.0.0
ENV SPAWN=true

ENTRYPOINT ["bundle", "exec"]
CMD ["ruby", "app.rb"]
