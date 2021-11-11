FROM ubuntu
MAINTAINER Mario Mainz

# install dependencies
RUN apt-get update
RUN apt-get -y install libpq-dev imagemagick phantomjs nginx

# install ruby from source
RUN apt-get -y install wget make build-essential g++
RUN wget http://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz
RUN tar -xzvf ruby-2.1.2.tar.gz
RUN cd ruby-2.1.2 && ./configure && make && make install

# install ruby gems
ADD ./Gemfile /var/www/discourse/Gemfile
ADD ./Gemfile.lock /var/www/discourse/Gemfile.lock
ADD ./vendor/ /var/www/discourse/vendor
RUN gem install bundler
RUN cd /var/www/discourse/ && bundle

# copy nginx config file
RUN rm /etc/nginx/sites-enabled/default
ADD /config/nginx.sample.conf /etc/nginx/sites-enabled/discourse.conf

# copy source to container
ADD . /var/www/discourse/

EXPOSE 80
EXPOSE 443

WORKDIR /var/www/discourse/
ENV DISCOURSE_DB_USERNAME postgres
CMD ["./docker-startup.sh"]
