FROM ruby:2.5

COPY . .
RUN bundle install

ENV PORT 1080
ENV HOST 0.0.0.0

EXPOSE 1080

CMD thin start -a $HOST -p $PORT
