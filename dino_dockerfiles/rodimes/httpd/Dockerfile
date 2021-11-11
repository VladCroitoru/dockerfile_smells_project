FROM httpd:alpine
MAINTAINER Rodrigo <rodimes@gmail.com>

ENV FOLDER=mydomain
ARG HTTPD_CONF_FILE=./confs/${FOLDER}/httpd.conf
ARG HTTPD_SSL_CONF_FILE=./confs/${FOLDER}/httpd-ssl.conf

COPY ${HTTPD_CONF_FILE} /usr/local/apache2/conf
COPY ${HTTPD_SSL_CONF_FILE} /usr/local/apache2/conf/extra
COPY /confs/letsencrypt_install.sh /usr/local/bin/

RUN echo '<META http-equiv="refresh" content="0;URL=/jenkins/">' > /usr/local/apache2/htdocs/index.html

RUN apk add --no-cache certbot

EXPOSE 80 443

ENTRYPOINT ["letsencrypt_install.sh"]

CMD ["httpd-foreground"]