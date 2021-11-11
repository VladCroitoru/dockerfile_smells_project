FROM ruby

RUN sed -i -e 's/jessie main/jessie main contrib non-free/' /etc/apt/sources.list
RUN sed -i -e 's/deb.debian.org/ftp.tsukuba.wide.ad.jp/' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y nano screen sudo git
RUN gem install bundler

RUN groupadd -g 1000 yi01
RUN useradd -m yi01 -u 1000 -g yi01 -G sudo
USER yi01
RUN mkdir /home/yi01/app

WORKDIR /home/yi01/app
RUN bundle init
RUN sed -i -e 's/# gem/gem/' Gemfile
RUN bundle install --path vendor/bundle
RUN bundle exec rails new . --api --skip-bundle --skip-test --force
RUN bundle install
RUN sed -i "/group :development, :test do/ a \ \ gem 'rspec-rails', '~> 3.5'" Gemfile
RUN sed -i "/group :development, :test do/ a \ \ gem 'factory_girl_rails'" Gemfile
RUN bundle install
RUN bundle exec rails generate rspec:install

RUN echo /vendor/bundle >> .gitignore
RUN echo /config/database.yml >> .gitignore

EXPOSE 3000
