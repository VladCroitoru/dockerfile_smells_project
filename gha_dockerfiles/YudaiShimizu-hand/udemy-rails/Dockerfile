# rails2.7.0を指定
FROM ruby:2.7.0
# パッケージインストール
RUN apt-get update -qq && apt-get install -y nodejs postgresql-client
RUN mkdir /udemy-rails
WORKDIR /udemy-rails
COPY Gemfile /udemy-rails/Gemfile
COPY Gemfile.lock /udemy-rails/Gemfile.lock
RUN bundle install
COPY . /udemy-rails

COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 3000

# rails起動コマンド
CMD ["rails", "server", "-b", "0.0.0.0"]