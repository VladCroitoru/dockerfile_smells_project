FROM ruby:2.6.5

## nodejsとyarnはwebpackをインストールする際に必要
# yarnパッケージ管理ツールをインストール

RUN curl http://deb.debian.org/debian/dists/buster/main/binary-amd64/by-hash/SHA256/935deda18d5bdc25fb1813d0ec99b6e0e32a084b203e518af0cf7dc79ee8ebda | head

RUN apt-get update && apt-get install -y curl apt-transport-https wget && \
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
apt-get update && apt-get install -y yarn  && apt-get install -y graphviz

# chromeの追加
RUN apt-get update && apt-get install -y unzip && \
    CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget -N http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip -P ~/ && \
    unzip ~/chromedriver_linux64.zip -d ~/ && \
    rm ~/chromedriver_linux64.zip && \
    chown root:root ~/chromedriver && \
    chmod 755 ~/chromedriver && \
    mv ~/chromedriver /usr/bin/chromedriver && \
    sh -c 'wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -' && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && apt-get install -y google-chrome-stable

RUN /bin/sh -c /bin/sh -c bundle update --bundler
RUN gem install bundler:2.1.4

RUN mkdir /coffee_passport
WORKDIR /coffee_passport
COPY Gemfile /coffee_passport/Gemfile
COPY Gemfile.lock /coffee_passport/Gemfile.lock
RUN bundle update rails
RUN bundle update
RUN bundle update mimemagic
RUN bundle update capybara selenium-webdriver
#RUN bundle update nokogiri marcel mimemagic
RUN bundle install

COPY . /coffee_passport

RUN yarn install --check-files
RUN bundle install
RUN bundle exec rails webpacker:compile

# Add a script to be executed every time the container starts.
COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 3000

# Start the main process.
CMD ["rails", "server", "-b", "0.0.0.0"]