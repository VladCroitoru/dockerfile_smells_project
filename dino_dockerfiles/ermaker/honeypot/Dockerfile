FROM ruby:onbuild

ENV WEB_CONCURRENCY=4
ENV RAILS_ENV=production
ENV PORT=5000

RUN rake assets:precompile assets:clean

EXPOSE 5000
CMD ["foreman", "start"]

# Workaround of https://github.com/bundler/bundler/issues/4576
RUN gem install bundler
