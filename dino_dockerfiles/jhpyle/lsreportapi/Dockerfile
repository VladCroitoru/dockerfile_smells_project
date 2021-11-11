FROM debian:jessie
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update
RUN until apt-get -q -y install locales python git apache2 supervisor perl libcgi-pm-perl libjson-perl fontconfig libfontconfig1 cron bzip2; do sleep 1; done
COPY phantomjs-2.1.1-linux-x86_64.tar.bz2 /tmp/
RUN mkdir -p /opt/lsreportapi && cd /opt && tar -xf /tmp/phantomjs-2.1.1-linux-x86_64.tar.bz2 && ln -s /opt/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs && git clone git://github.com/casperjs/casperjs.git && ln -s /opt/casperjs/bin/casperjs /usr/local/bin/casperjs
RUN chown -R www-data.www-data /var/www && chsh -s /bin/bash www-data
RUN cd /opt && git clone https://github.com/letsencrypt/letsencrypt && cd letsencrypt && ./letsencrypt-auto --help
COPY initialize.sh /opt/lsreportapi/
COPY cron-weekly.sh /etc/cron.weekly/renew-letsencrypt
COPY apache.key /etc/ssl/apache.key
COPY apache.crt /etc/ssl/apache.crt
COPY ls-report-api.js /opt/lsreportapi/
COPY index.pl /var/www/
COPY default-ssl.conf /opt/lsreportapi/
COPY default.conf /opt/lsreportapi/
COPY supervisor.conf /etc/supervisor/conf.d/lsreportapi.conf

USER root
RUN a2enmod ssl
RUN a2enmod rewrite
RUN a2enmod cgid
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN locale-gen
RUN update-locale LANG=en_US.UTF-8
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
EXPOSE 80
EXPOSE 443

VOLUME  ["/etc/letsencrypt", "/etc/apache2/sites-available"]

CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
