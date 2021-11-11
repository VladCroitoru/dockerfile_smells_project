FROM ruby:2.1
RUN apt-get update && apt-get install -y ruby2.1 zlib1g-dev build-essential imagemagick ruby-rmagick libmagickcore-dev libmagickwand-dev nodejs libruby2.1 libsqlite3-dev libmysqlclient-dev libmysqlclient18 git libxslt-dev
RUN git clone https://github.com/concerto/concerto.git
RUN cd concerto && git checkout tags/2.3.5 -b 235 && (bundle install --path vendor/bundle || bundle update concerto_remote_video || bundle update concerto_simple_rss )
RUN gem install bundler
WORKDIR /concerto
#RAILS_ENV=production bundle exec rake db:migrate && RAILS_ENV=production bundle exec rake db:seed && RAILS_ENV=production bundle exec rake assets:precompile


