FROM houseofagile/docker-nginx-php-fpm:latest

MAINTAINER Meillaud Jean-Christophe (jc@houseofagile.com)

RUN export TERM=xterm
RUN curl -SsL https://download.owncloud.org/download/repositories/stable/Ubuntu_14.04/Release.key | sudo apt-key add -

RUN sh -c "echo 'deb http://download.owncloud.org/download/repositories/stable/Ubuntu_14.04/ /' >> /etc/apt/sources.list.d/owncloud.list" && \
  apt-get update && \
  apt-get install -y owncloud


ADD ./conf/default-owncloud-nginx.conf /etc/nginx/sites-available/default-owncloud-nginx.conf

RUN  ln -s /etc/nginx/sites-available/default-owncloud-nginx.conf /etc/nginx/sites-enabled/default-owncloud-nginx.conf && \
  rm /etc/nginx/sites-enabled/default && \
  sed -i -e "s/^upload_max_filesize\s*=\s*2M/upload_max_filesize = 512M/" /etc/php5/fpm/php.ini && \
  sed -i -e "s/^post_max_size\s*=\s*8M/post_max_size = 512M/" /etc/php5/fpm/php.ini

RUN mkdir -p /etc/my_init.d
ADD setup-owncloud.sh /etc/my_init.d/10_setup-owncloud.sh

EXPOSE 80
CMD ["/sbin/my_init"]
