FROM jekyll/builder

WORKDIR /tmp
ADD Gemfile /tmp/
RUN bundle install

VOLUME /src
EXPOSE 4000

WORKDIR /src
ENTRYPOINT ["bundle", "exec", "jekyll", "serve", "--watch", "--force_polling" , "-H", "0.0.0.0"]
