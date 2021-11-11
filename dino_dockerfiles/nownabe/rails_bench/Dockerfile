FROM nownabe/ruby:2.2.0-nginx
MAINTAINER nownabe

# Install Percona
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A
RUN echo 'deb http://repo.percona.com/apt wheezy main' >> /etc/apt/sources.list
RUN echo 'deb-src http://repo.percona.com/apt wheezy main' >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y percona-xtradb-cluster-client-5.6

RUN rm -rf /var/lib/apt/lists/*

RUN bundle config --global frozen 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY Gemfile /usr/src/app/
COPY Gemfile.lock /usr/src/app/
RUN bundle install --without=develop,test

COPY . /usr/src/app
COPY nginx.conf /etc/nginx/conf.d/app.conf
RUN mkdir -p tmp/pids tmp/sockets

EXPOSE 80
CMD ["/usr/src/app/bootstrap.sh"]

