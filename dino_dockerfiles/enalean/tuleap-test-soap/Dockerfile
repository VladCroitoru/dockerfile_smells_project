## Re-use tuleap base for caching ##
FROM centos:centos6

MAINTAINER Manuel Vacelet, manuel.vacelet@enalean.com
MAINTAINER Yannis ROSSETTO, yannis.rossetto@enalean.com

COPY Tuleap.repo /etc/yum.repos.d/

RUN yum -y install epel-release && \
    yum -y install php \
    php-soap \
    php-mysql \
    php-gd \
    php-process \
    php-xml \
    php-pecl-xdebug  \
    php-mbstring \
    mysql-server \
    httpd \
    php-password-compat \
    php-paragonie-random-compat \
    php-zendframework \
    php-ZendFramework2-Loader \
    htmlpurifier \
    jpgraph-tuleap && \
    yum clean all

RUN service mysqld start && sleep 1 && mysql -e "GRANT ALL PRIVILEGES on *.* to 'integration_test'@'localhost' identified by 'welcome0'"

RUN curl -k -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin

COPY soap-tests.conf /etc/httpd/conf.d/soap-tests.conf

COPY composer.json /tmp/run/composer.json
RUN cd /tmp/run && php /usr/local/bin/composer.phar install

ADD run.sh /run.sh
ENTRYPOINT ["/run.sh"]

VOLUME ["/tuleap"]

# We can use volumes when cp from volumes will be supported
#VOLUME ["/output"]
