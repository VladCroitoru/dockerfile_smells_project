FROM nitrousio/ruby:latest
MAINTAINER Mike Chelen <michael.chelen@gmail.com>

RUN \
  apt-get install -y libpq-dev


RUN \
  su action -l -c /bin/bash -c \
  'rbenv install 2.1.2 && \
  rbenv global 2.1.2 && \
  gem install bundler rails && \
  git clone https://github.com/ploslabs/rich_citations.git && \
  cd rich_citations && \
  bundle install && \
  cp config/database.example.yml config/database.yml && \
  bundle exec rake db:migrate'
  
USER \
  action
  
WORKDIR \
  /home/action/rich_citations/

CMD \
  /bin/bash -c 'source /etc/profile && bundle exec rails server'
