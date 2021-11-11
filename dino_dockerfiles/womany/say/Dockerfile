FROM    ruby:2.2

expose  7777

RUN     apt-get update
RUN     apt-get install --force-yes -y imagemagick
RUN     gem install bundler

RUN     mkdir -p /docker-app
WORKDIR /docker-app
ADD     . /docker-app

RUN     bundle install --without development
CMD     ["rainbows", "-N", "-E", "production", "-p", "7777", "-c", "rainbows.rb", "config.ru"]
