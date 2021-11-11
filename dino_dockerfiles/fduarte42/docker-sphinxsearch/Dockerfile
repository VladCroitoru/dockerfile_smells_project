FROM ubuntu:18.04

ENV TERM "dumb"

RUN apt-get update && apt-get upgrade -y && apt-get install -y sphinxsearch wget php7.2-cli php7.2-xmlreader php7.2-zip php7.2-curl php7.2-intl php7.2-mysql
RUN apt-get install -y cron supervisor
RUN wget http://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
RUN tar xvfz ioncube_loaders_lin_x86-64.tar.gz
RUN cp ioncube/ioncube_loader_lin_7.2.so /usr/lib/php/20170718
RUN echo 'zend_extension = "/usr/lib/php/20170718/ioncube_loader_lin_7.2.so"' > /etc/php/7.2/mods-available/ioncube_loader.ini && echo '; priority=1' >> /etc/php/7.2/mods-available/ioncube_loader.ini
RUN phpenmod ioncube_loader
RUN rm ioncube_loaders_lin_x86-64.tar.gz
RUN rm -R ioncube

RUN mkdir /var/www
RUN mkdir /var/www/html

COPY cron-foreground /usr/local/bin/cron-foreground
RUN chmod 700 /usr/local/bin/cron-foreground
COPY searchd-foreground /usr/local/bin/searchd-foreground
RUN chmod 755 /usr/local/bin/searchd-foreground
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

VOLUME ["/var/lib/sphinxsearch/data"]

EXPOSE 9312 9306

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

