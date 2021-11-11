FROM tutum/lamp:latest

ENV DEBIAN_FRONTEND noninteractive 
ENV DVWA_VERSION master

ADD entrypoint.sh .
RUN chmod +x /entrypoint.sh

# Requirements
RUN rm -fr /app/* \
    && apt-get update \
    && apt-get install -yqq wget unzip php5-gd build-essential \
    && rm -rf /var/lib/apt/lists/*

# DVWA installation
RUN wget https://github.com/ethicalhack3r/DVWA/archive/$DVWA_VERSION.zip \
    && unzip $DVWA_VERSION.zip \
    && rm -rf app/* \
    && cp -r /DVWA-$DVWA_VERSION/* /app \
    && rm -rf /DVWA-$DVWA_VERSION \
    && chmod a+w /app/hackable/uploads/ \
    && chmod a+w /app/external/phpids/0.6/lib/IDS/tmp/phpids_log.txt

# DVWA configuration
RUN sed -i "s/^\$_DVWA\[ 'db_user' \]     = 'root'/\$_DVWA\[ 'db_user' \]     = 'admin'/g" /app/config/config.inc.php.dist \
    && sed -i "s/^\$_DVWA\[ 'recaptcha_public_key' \]  = ''/\$_DVWA\[ 'recaptcha_public_key' \]  = '6LdK7xITAAzzAAJQTfL7fu6I-0aPl8KHHieAT_yJg'/g" /app/config/config.inc.php.dist \
    && sed -i "s/^\$_DVWA\[ 'recaptcha_private_key' \] = ''/\$_DVWA\[ 'recaptcha_private_key' \] = '6LdK7xITAzzAAL_uw9YXVUOPoIHPZLfw2K1n5NVQ'/g" /app/config/config.inc.php.dist \
    && cp app/config/config.inc.php.dist app/config/config.inc.php \
    && sed -i "s/^allow_url_include = Off/allow_url_include = On/g" /etc/php5/apache2/php.ini \
    && echo "sed -i \"s/p@ssw0rd/\$PASS/g\" /app/config/config.inc.php" >> /create_mysql_admin_user.sh \
    && echo 'session.save_path = "/tmp"' >> /etc/php5/apache2/php.ini

ENV OSSEC_VERSION 2.8.3

# OSSEC installation
RUN wget https://bintray.com/artifact/download/ossec/ossec-hids/ossec-hids-$OSSEC_VERSION.tar.gz \
    && tar -xzf ossec-hids-$OSSEC_VERSION.tar.gz
WORKDIR ossec-hids-$OSSEC_VERSION
ENV TERM vt100
RUN echo -n "fr\n\nlocal\n/var/ossec\nn\no\no\nn\n" | ./install.sh

# OSSEC configuration
COPY ossec.conf /var/ossec/etc/
RUN grep 554 /var/ossec/rules/ossec_rules.xml | grep level | sed -i "s/0/7/" /var/ossec/rules/ossec_rules.xml

EXPOSE 80 3306

#CMD [ "/run.sh" ]
ENTRYPOINT [ "/entrypoint.sh" ]
