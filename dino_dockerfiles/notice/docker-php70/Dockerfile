FROM nimmis/apache-php7
MAINTAINER kan
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN apt-get update
RUN apt-get install -y language-pack-ja
RUN update-locale LANG=ja_JP.UTF-8
RUN cd /etc/apache2/mods-enabled && ln -sfn ../mods-available/rewrite.load .
COPY httpd.conf /etc/apache2/sites-available/000-default.conf
ENV LANG ja_JP.UTF-8
RUN rm -f /var/www/html/index.html
