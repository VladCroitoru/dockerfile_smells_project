FROM alpine:3.8

LABEL maintainer="Giuseppe Pellegrino <g.pellegrino@tadaweb.com>"

RUN apk update \
    && apk add lighttpd php5-common php5-gd php5-curl php5-cgi fcgi php5-pdo php5-dom php5-pear php5-dev php5-xml php5-json \
    && apk add autoconf gcc g++ make libffi-dev openssl-dev bash wget && rm -rf /var/cache/apk/* \
    && ln -s /usr/bin/php5 /usr/bin/php \
    && ln -s /usr/bin/php-cgi5 /usr/bin/php-cgi

RUN sed -i -e 's/-n//g' /usr/bin/pecl \
    && printf "\n" | pecl install mongo \
    && echo "extension=mongo.so" > /etc/php5/conf.d/mongo.ini \
    && wget --no-check-certificate https://github.com/iwind/rockmongo/archive/1.1.7.tar.gz \
    && tar -xzf 1.1.7.tar.gz \
    && rm 1.1.7.tar.gz \
    && mv rockmongo-1.1.7/ /var/www/localhost/rockmongo \
    && chown -R lighttpd:lighttpd /var/www/localhost/rockmongo/ \
    && chmod -R 777 /var/www/localhost/ \
    && chmod -R 777 /var/www/localhost/rockmongo/ \
    && mkdir -p /var/run/lighttpd && touch /var/run/lighttpd/php-fastcgi.socket && chown -R lighttpd:lighttpd /var/run/lighttpd \
    && sed -i -e 's/htdocs"/rockmongo"/g' /etc/lighttpd/lighttpd.conf \
    && sed -i -e 's/#   include "mod_fastcgi.conf"/include "mod_fastcgi.conf"/g' /etc/lighttpd/lighttpd.conf \
    && sed -i -e 's/#    "mod_rewrite",/    "mod_rewrite",/g' /etc/lighttpd/lighttpd.conf \
    && sed -i -e 's/#    "mod_alias",/    "mod_alias",/g' /etc/lighttpd/lighttpd.conf \
    && sed -i -e '/server.pid-file/a server.port          = env.ROCKMONGO_PORT' /etc/lighttpd/lighttpd.conf \
    && sed -i -e 's/\/run\/lighttpd\/lighttpd-fastcgi-php-" + PID + ".socket/\/var\/run\/lighttpd\/php-fastcgi.socket/g' /etc/lighttpd/mod_fastcgi.conf

COPY config.php /var/www/localhost/rockmongo/config.php

RUN chmod +x /var/www/localhost/rockmongo/config.php

ENV ROCKMONGO_PORT 8050
ENV MONGO_HOSTS localhost:27017

EXPOSE 8050

CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]
