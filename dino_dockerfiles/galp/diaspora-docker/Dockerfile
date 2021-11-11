FROM ruby:2.3

RUN echo "deb http://http.debian.net/debian jessie-backports main" >> /etc/apt/sources.list \
     && echo 'APT::Install-Recommends "0";' > /etc/apt/apt.conf.d/99norecommends \
     && apt-get update && apt-get install -y \
     build-essential cmake libssl-dev libcurl4-openssl-dev \
     libxml2-dev libxslt-dev imagemagick ghostscript curl \
     libmagickwand-dev git libpq-dev redis-server nodejs \
     supervisor nginx-light ca-certificates

RUN adduser --disabled-login --home /home/diaspora diaspora

RUN cd /home/diaspora ; su -c "git clone -b master https://github.com/diaspora/diaspora.git" diaspora
WORKDIR /home/diaspora/diaspora

COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY docker/nginx.conf  /etc/nginx/nginx.conf
COPY docker/diaspora.yml ./config/diaspora.yml
COPY docker/database.yml ./config/database.yml

RUN su -c "RAILS_ENV=production bundle install --jobs $(nproc) --deployment --without test development --with postgresql" diaspora
RUN su -c "RAILS_ENV=production bin/rake assets:precompile" diaspora
#RUN RAILS_ENV=production bin/rake db:create db:schema:load

#RUN mkdir /etc/certs && openssl dhparam 2048 > /etc/certs/dhparam.pem
VOLUME /etc/letsencrypt /home/diaspora/diaspora/public/uploads
EXPOSE 80 443 5269
CMD ["/usr/bin/supervisord"]


