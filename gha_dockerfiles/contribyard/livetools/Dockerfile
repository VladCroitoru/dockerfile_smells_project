FROM ruby:3.0.2

RUN gem install bundler

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    echo 'deb https://dl.yarnpkg.com/debian/ stable main' > /etc/apt/sources.list.d/yarn.list &&\
    wget -q -O - https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - &&\
    apt-get update -qq && \
    apt-get install -y build-essential nodejs yarn

WORKDIR /var/app

COPY . .

RUN bundler install

ENTRYPOINT ["./entrypoint.sh"]