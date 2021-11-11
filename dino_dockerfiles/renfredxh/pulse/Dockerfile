FROM ubuntu:14.04

RUN apt-get update && apt-get -qy install curl nano git build-essential unzip \
nodejs sqlite3 libsqlite3-dev

## Install ruby using rvm
# Import gpg key and run rvm install script
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3 && curl -sSL https://get.rvm.io | bash -s stable
# install RVM, Ruby, and Bundler
RUN \curl -L https://get.rvm.io | bash -s stable
RUN bash -c -l "rvm requirements"
RUN bash -c -l "rvm install 2.1"
RUN bash -c -l "gem install bundler rake --no-ri --no-rdoc"
RUN bash -c -l "bundle config path \"$HOME/bundler\""

RUN git clone https://github.com/renfredxh/pulse.git
WORKDIR /pulse

RUN bash -c -l "bundle install"

# Download the default sqlite database and samples
ADD https://dl.dropboxusercontent.com/u/3672377/data/pulse/production.sqlite3 /pulse/db/production.sqlite3
ADD https://dl.dropboxusercontent.com/u/3672377/data/pulse/media.tar.gz /pulse/public/
RUN mkdir /pulse/public/media && tar -zxvf /pulse/public/media.tar.gz -C /pulse/public/

EXPOSE 80
# Run unicorn server on port 80
CMD bash -c -l "bundle exec unicorn_rails -p 80 -E production"
