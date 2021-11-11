FROM ruby:3.0.2
RUN apt-get update -qq && apt-get install -y --no-install-recommends nodejs default-mysql-client && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y curl apt-transport-https wget && \
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
apt-get update && apt-get install -y yarn
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
apt-get install -y nodejs
RUN mkdir /okonomiyakidb
WORKDIR /okonomiyakidb
COPY ./ /okonomiyakidb/

RUN gem install bundler
RUN bundle install
RUN rails webpacker:install


COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 3000

CMD ["rails", "server", "-b", "0.0.0.0"]