FROM malfurious/nginx-php

LABEL description "Roundcube-Postfix is a simple, modern & fast webmail client combined with an administrative Postfixadmin webportal to manage postfix accounts." \
      maintainer="Malfurious <jmay9990@gmail.com>"
	  
ARG ROUND_VERSION=1.3.4
ARG POST_VERSION=3.1
ENV UID=991 GID=991 UPLOAD_MAX_SIZE=25M MEMORY_LIMIT=128M
ENV PLUGINS=" 'password','enigma','emoticons','filesystem_attachments','managesieve','identity_smtp','calendar','contextmenu','markasjunk2','tasklist','persistent_login'"
RUN echo "@community https://nl.alpinelinux.org/alpine/v3.6/community" >> /etc/apk/repositories \
 && apk -U upgrade
RUN apk add gnupg openssl dovecot tini@community
RUN apk add -t build-dependencies \
    wget \
    git \
    curl \
	ca-certificates \
	coreutils \
	gcc \
	linux-headers \
	make \
	musl-dev \
 && cd /tmp \
 && wget -q https://github.com/roundcube/roundcubemail/releases/download/${ROUND_VERSION}/roundcubemail-${ROUND_VERSION}-complete.tar.gz \
 && wget -q https://downloads.sourceforge.net/project/postfixadmin/postfixadmin/postfixadmin-${POST_VERSION}/postfixadmin-${POST_VERSION}.tar.gz \
 && git clone https://git.kolab.org/diffusion/RPK/roundcubemail-plugins-kolab.git
RUN mkdir /roundcube && tar -xzf /tmp/roundcubemail-${ROUND_VERSION}-complete.tar.gz --strip 1 -C /roundcube \
 && mv /roundcube/config/config.inc.php.sample /roundcube/config/config.inc.php && mv /roundcube/composer.json-dist /roundcube/composer.json
RUN mkdir /postfixadmin && tar xzf /tmp/postfixadmin-${POST_VERSION}.tar.gz -C /postfixadmin && mv /postfixadmin/postfixadmin-${POST_VERSION}/* /postfixadmin
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/roundcube/ --filename=composer.phar
RUN cd /roundcube && php composer.phar install --no-dev && php composer.phar require sabre/vobject 3.3.3 \
 && cd /roundcube/plugins && git clone git://github.com/elm/Roundcube-SMTP-per-Identity-Plugin.git identity_smtp \
 && cp -r /tmp/roundcubemail-plugins-kolab/plugins/calendar . && cp -r /tmp/roundcubemail-plugins-kolab/plugins/libcalendaring . && cp -r /tmp/roundcubemail-plugins-kolab/plugins/tasklist . \
 && cd /roundcube/plugins/calendar && cp config.inc.php.dist config.inc.php 
RUN cd /roundcube/plugins && git clone https://github.com/JohnDoh/Roundcube-Plugin-Context-Menu.git contextmenu \
 && git clone https://github.com/JohnDoh/Roundcube-Plugin-Mark-as-Junk-2.git markasjunk2 && git clone https://github.com/mfreiholz/persistent_login.git persistent_login \
 && find /roundcube -type d -exec chmod 755 {} \; \
 && find /roundcube -type f -exec chmod 644 {} \;
RUN mkdir /enigma && mv /roundcube/plugins/password/config.inc.php.dist /roundcube/plugins/password/config.inc.php \
 && mv /roundcube/plugins/enigma/config.inc.php.dist /roundcube/plugins/enigma/config.inc.php \
 && mv /roundcube/plugins/tasklist/config.inc.php.dist /roundcube/plugins/tasklist/config.inc.php \
 && mv /roundcube/plugins/persistent_login/config.inc.php.dist /roundcube/plugins/persistent_login/config.inc.php
RUN apk del build-dependencies \
 && rm -rf /tmp/* /var/cache/apk/* /root/.gnupg /postfixadmin/postfixadmin-${POST_VERSION}*
RUN sed -i "/'zipdownload',/a ${PLUGINS}" /roundcube/config/config.inc.php
COPY rootfs /
COPY mysql.initial.sql /roundcube/SQL
RUN chmod +x /usr/local/bin/* /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*
EXPOSE 8888 8080
VOLUME /enigma
CMD ["tini", "--", "run.sh"]
