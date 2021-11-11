FROM eboraas/phalcon

# Note: "default" is enabled in the default installation, and "default-ssl" is enabled in the eboraas/apache image, so no need to recreate the symlinks here, just copy the new site definitions into place
ADD default /etc/apache2/sites-available/
ADD default-ssl /etc/apache2/sites-available/

RUN rm -f /etc/apache2/sites-available/000-default.conf
RUN ln -s /etc/apache2/sites-available/default /etc/apache2/sites-available/000-default.conf
RUN apt-get install -y php5-mysql
RUN apt-get install -y php5-curl

EXPOSE 80
EXPOSE 443

VOLUME /var/www/phalcon
WORKDIR /var/www/phalcon/public
RUN /bin/echo '<html><body><h1>It works!</h1></body></html>' > /var/www/phalcon/public/index.html

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]