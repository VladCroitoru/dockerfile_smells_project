FROM bretfisher/jekyll-serve

COPY Gemfile .
COPY Gemfile.lock .

RUN bundle install

CMD [ "bundle", "exec", "jekyll", "serve", "--force_polling", "-H", "0.0.0.0", "-P", "4000" ]