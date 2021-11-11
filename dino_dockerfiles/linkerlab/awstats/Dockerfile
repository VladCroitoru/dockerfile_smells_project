From peihsinsu/nodejs

RUN apt-get update -y && apt-get install apache2 -y && \
  cd / && \
  wget http://prdownloads.sourceforge.net/awstats/awstats-7.3.tar.gz && \
  tar zxvf awstats-7.3.tar.gz && \
  cd awstats-7.3/wwwroot/ && \
  mkdir -p /var/www/html/awstats && \
  mkdir -p /var/www/html/icon && \
  cp -r /awstats-7.3/wwwroot/icon /var/www/html/ && \
  chown www-data:www-data -R /var/www/html/icon/ && \
#  service apache2 restart && \
  a2enmod cgi && \
  mv cgi-bin awstats && \
  chown www-data:www-data -R awstats && \ 
  mv awstats /usr/lib/cgi-bin 

ADD ./awstats.linoxide.conf /usr/lib/cgi-bin/awstats/awstats.linoxide.conf
ADD ./run.sh /

WORKDIR /

CMD /run.sh
