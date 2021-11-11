FROM paolodenti/jessie-apt-utils:8.7

MAINTAINER Paolo Denti "paolo.denti@gmail.com"

RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y apache2
RUN a2enmod proxy_http
RUN a2enmod proxy_html
RUN a2enmod xml2enc

# cleanup
RUN rm -rf /var/lib/apt/lists/*

COPY 000-default.conf /etc/apache2/sites-available/

EXPOSE 80

ENV PROXY_HOST 127.0.0.1
ENV PROXY_PORT 8080

COPY start.sh /start.sh
RUN chmod 0755 /start.sh
CMD ["bash", "/start.sh"]
