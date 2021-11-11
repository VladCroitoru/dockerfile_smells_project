FROM ubuntu:14.04
MAINTAINER Kamil Manka <kamil.manka@gmail.com>

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install unzip curl

ADD run.sh /run.sh
RUN chmod +x /run.sh
RUN mkdir -p /var/www/html

# apache config
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
RUN chown -R www-data:www-data /var/www/

VOLUME /var/www/html

ENTRYPOINT ["/run.sh"]
