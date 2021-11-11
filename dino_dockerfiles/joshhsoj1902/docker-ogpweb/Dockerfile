FROM nimmis/apache-php5:latest@sha256:712d35d5cc30e6a911e260e871f08f77d5684edcc50cba21163535714c547ff5

RUN apt-get update
RUN apt-get install -y php5-mysql php5-xmlrpc php-pear

RUN curl -sSLf -z /usr/local/bin/gomplate -o /usr/local/bin/gomplate https://github.com/hairyhenderson/gomplate/releases/download/v2.0.0/gomplate_linux-amd64-slim \
  && chmod 755 /usr/local/bin/gomplate

RUN wget -P ~/public_html https://github.com/OpenGamePanel/OGP-Website/archive/5df2685bf9e39e10ba2df046d78f25717fa4b8b4.zip \
  && unzip ~/public_html/5df2685bf9e39e10ba2df046d78f25717fa4b8b4.zip -d ~/public_html \
  && rm -rf /var/www/html \
  && cp -rp ~/public_html/OGP-Website-5df2685bf9e39e10ba2df046d78f25717fa4b8b4 /var/www/html \
  && rm -rf ~/public_html

COPY templates /var/templates
ADD docker-runner.sh docker-health.sh installer.sh was-installer-removed.sh /

RUN chmod +x /installer.sh /was-installer-removed.sh

RUN chmod -R 777 /var/www/html/modules/TS3Admin/templates_c /docker-health.sh
RUN mv /var/www/html/install.php /var/www/html/install.php.bac

WORKDIR /

HEALTHCHECK --start-period=45s CMD /docker-health.sh

CMD ["sh", "/docker-runner.sh"]
