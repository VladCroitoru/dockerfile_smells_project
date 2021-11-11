FROM debian:jessie
MAINTAINER tyler.hoadley[AT]computersthatwork[DOT]ca
RUN apt-get update && apt-get install -y php5 libapache2-mod-php5 php5-cli php-gettext php-tcpdf php5-cli php5-common php5-gd php5-json php5-mcrypt php5-mysql php5-readline && apt-get clean && rm -rf /var/lib/apt/lists/*
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ONBUILD ADD . /var/www/html/
EXPOSE 80
ENTRYPOINT ["/usr/sbin/apache2"]
CMD ["-D", "FOREGROUND"]
