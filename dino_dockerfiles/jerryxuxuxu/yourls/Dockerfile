FROM tutum/apache-php

RUN rm -fr /app

ENV YOURLS_VERSION 1.7.1

RUN curl -o /tmp/YOURLS-$YOURLS_VERSION.tar.gz -L https://github.com/YOURLS/YOURLS/archive/$YOURLS_VERSION.tar.gz
RUN tar -zxf /tmp/YOURLS-$YOURLS_VERSION.tar.gz --strip-components=1
RUN rm /tmp/YOURLS-$YOURLS_VERSION.tar.gz
RUN a2enmod rewrite

ADD .htaccess /app/
