FROM polleverywhere/rbenv

MAINTAINER Matthias Pfeil <matthias.pfeil@wwu.de>

RUN apt-get update && apt-get install --fix-missing -q -y --force-yes git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libpq-dev libxslt1-dev libmysqlclient-dev libcurl4-openssl-dev python-software-properties nodejs imagemagick

RUN rbenv install 1.9.3-p550 && rbenv global 1.9.3-p550

RUN gem install bundler --no-ri --no-rdoc
RUN rbenv rehash

RUN git clone https://github.com/frab/frab.git ~/frab && cd ~/frab/ && rbenv local 1.9.3-p550 && bundle install && cp config/database.yml.template config/database.yml && cp config/settings.yml.template config/settings.yml && rake db:setup && rake secret && cp config/initializers/secret_token.rb.example config/initializers/secret_token.rb

EXPOSE 3000

WORKDIR /root/frab/

CMD ["rails","server"]