from ubuntu

RUN apt-get update && \
    apt-get install -y apache2

ADD ./html/* /var/www/html/
COPY run-apache /run-apache
RUN chmod a+x /run-apache

EXPOSE 80
CMD ["/run-apache"]
