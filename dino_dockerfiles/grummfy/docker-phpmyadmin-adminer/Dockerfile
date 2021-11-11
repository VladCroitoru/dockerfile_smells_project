FROM corbinu/docker-phpmyadmin
MAINTAINER Grummfy me@grummfy.be

ENV ADMINER_VERSION 4.2.3

RUN wget https://www.adminer.org/static/download/${ADMINER_VERSION}/adminer-${ADMINER_VERSION}.php \
 && mv adminer-${ADMINER_VERSION}.php /www/adminer.php

