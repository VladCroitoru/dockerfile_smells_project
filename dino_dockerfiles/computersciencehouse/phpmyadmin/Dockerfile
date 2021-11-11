FROM centos/php-70-centos7:latest
MAINTAINER Christophe LARUE <dev@startx.fr>

USER root
ENV APP_PATH=/opt/app-root/src
RUN cd $APP_PATH && \
    wget -q https://files.phpmyadmin.net/phpMyAdmin/4.7.3/phpMyAdmin-4.7.3-all-languages.zip && \
    unzip phpMyAdmin-4.7.3-all-languages.zip && \
    rm -f phpMyAdmin-4.7.3-all-languages.zip && \
    mv phpMyAdmin-4.7.3-all-languages/* ./  && \
    rm -rf phpMyAdmin-4.7.3-all-languages && \
    rm -f config.sample.inc.php && \
    chown -R 1001:0 $APP_PATH && \
    chmod -R ug+rwx $APP_PATH
COPY config.inc.php $APP_PATH/config.inc.php

USER 1001
EXPOSE 8080
CMD $STI_SCRIPTS_PATH/run