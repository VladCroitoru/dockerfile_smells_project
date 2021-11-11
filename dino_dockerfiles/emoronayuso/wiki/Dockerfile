# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage:0.9.17

MAINTAINER Enrique Moron Ayuso "enrique@quaip.com"

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# ...put your own build instructions here...
RUN apt-get update
RUN apt-get install -y vim-nox php5-fpm php5-intl php5-gd php5-pgsql php5-xcache nginx postgresql

RUN curl -O http://releases.wikimedia.org/mediawiki/1.25/mediawiki-1.25.2.tar.gz \
    && tar xvzf mediawiki-*.tar.gz \
    && mv mediawiki-1.25.2/* /usr/share/nginx/html/

RUN sed  -e 's/#location\ \~\ \\\.php/location\ \~\ \\\.php/g'         \
         -e 's/#\tfastcgi_split_path_info/fastcgi_split_path_info/g'   \
         -e 's/#\tfastcgi_pass\ unix/fastcgi_pass\ unix/g'             \
         -e 's/#\tfastcgi_index/fastcgi_index/g'                       \
         -e 's/\tindex\ index.html/index\ index.php\ index.html/g'                 \
         -e 's/#\tinclude\ fastcgi_params;/include\ fastcgi_params;}/g' -i /etc/nginx/sites-available/default

RUN sed -e 's/shared_buffers\ =\ 128MB/shared_buffers = 100MB/g' -i /etc/postgresql/9.3/main/postgresql.conf 

USER postgres

RUN /etc/init.d/postgresql start && \
      psql --command "CREATE USER wiki WITH NOCREATEDB NOCREATEROLE NOSUPERUSER ENCRYPTED PASSWORD 'hackmeplease';" && \ 
      psql --command "CREATE DATABASE wiki WITH OWNER wiki;"

USER root

RUN echo \#\!/bin/bash >> /etc/my_init.d/start.sh
RUN echo /etc/init.d/nginx restart >> /etc/my_init.d/start.sh
RUN echo /etc/init.d/postgresql restart >> /etc/my_init.d/start.sh 
RUN echo /etc/init.d/php5-fpm restart >> /etc/my_init.d/start.sh
RUN echo echo tail -f \> /dev/null >> /etc/my_init.d/start.sh
RUN echo exit 0 >> /etc/my_init.d/start.sh
RUN chmod +x /etc/my_init.d/start.sh

EXPOSE 80

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

