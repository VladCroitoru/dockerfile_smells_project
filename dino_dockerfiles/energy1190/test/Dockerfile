FROM debian:stretch

ENV DOKUWIKI_VERSION=2017-02-19e

ADD entrypoint.sh /entrypoint.sh
ADD dokuwiki.conf /etc/apache2/sites-available/dokuwiki.conf
ADD /etc /etc/dokuwiki

RUN apt-get update && \
    apt-get install -y apache2 curl php7.0 libapache2-mod-php7.0 php7.0-mcrypt php7.0-cli php7.0-ldap php7.0-xml

RUN curl -s -o dokuwiki.tgz https://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz \
    && tar -xvzf ./dokuwiki.tgz \
    && rm -f ./dokuwiki.tgz

RUN cp -r ./dokuwiki-${DOKUWIKI_VERSION} /usr/share/dokuwiki \
    && rm -rf ./dokuwiki-${DOKUWIKI_VERSION} \
    && rm -rf /usr/share/dokuwiki/lib/plugins \
    && rm -rf /usr/share/dokuwiki/lib/tpl

RUN a2dissite 000-default \
    && a2ensite dokuwiki

RUN mkdir -p /var/lib/dokuwiki \
    && chown www-data:www-data -R /etc/dokuwiki \
    && chown www-data:www-data -R /var/lib/dokuwiki \
    && chown www-data:www-data -R /usr/share/dokuwiki \
    && chmod +x /entrypoint.sh
	
ADD preload.php /usr/share/dokuwiki/inc/preload.php

EXPOSE 80

CMD ["/entrypoint.sh"]
