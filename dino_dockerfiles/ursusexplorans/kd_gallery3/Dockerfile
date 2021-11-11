FROM debian:wheezy

ENV DEBIAN_FRONTEND noninteractive

RUN \
  apt-get update && \
  apt-get install -y \
      apache2 \
      libapache2-mod-php5 \
      php5-mysql \
      imagemagick \
      graphicsmagick \
      dcraw \
      ffmpeg \
      git \
      libjs-jquery \
      libjs-jquery-ui \
      mysql-client \
      wwwconfig-common \
      dbconfig-common && \
   apt-get clean autoclean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

RUN \
  git clone https://github.com/gallery/gallery3.git && \ 
  cd /gallery3 && git checkout 3.0.9 && rm -rf .git 

RUN \
  git clone https://github.com/gallery/gallery3-contrib.git && \
  mv /gallery3-contrib/3.0/modules/* /gallery3/modules/ && rm -rf /gallery3-contrib

RUN git clone https://github.com/mstoltenburg/html5_upload_progress.git && mv html5_upload_progress /gallery3/modules/
RUN git clone https://github.com/mrJakez/gallery3-extended_rest.git && mv gallery3-extended_rest /gallery3/modules/

#RUN \
#  git clone https://github.com/avolf/gallery-html5video.git && \
#  mv /gallery-html5video/html5video /gallery3/modules/  && rm -rf /gallery-html5video

RUN rm -rf /var/www/*
RUN cp -r /gallery3/. /var/www/ 
RUN rm -rf /gallery3 

RUN a2enmod rewrite
RUN a2enmod expires
ADD /apache-default /etc/apache2/sites-available/default

ADD htaccess /var/www/.htaccess
ADD php.ini /etc/php5/apache2/php.ini

RUN chown -R www-data:www-data /var/www/*

VOLUME ["/var/www/var"]

ADD entrypoint.sh /entrypoint.sh

ENTRYPOINT /entrypoint.sh
