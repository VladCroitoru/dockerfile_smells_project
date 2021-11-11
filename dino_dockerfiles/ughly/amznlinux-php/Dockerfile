FROM amazonlinux

MAINTAINER Chris Yawman <chris.yawman@team.neustar>

RUN yum install -y epel-release git wget patch

RUN yum -y install php70-cli php70-common php70-json php70-gd php70-intl php70-mbstring php70-mcrypt php70-mysqlnd php70-ldap php70-pdo php70-pear php70-pgsql php70-process php70-soap php70-pecl-xdebug php70-xml php70-xsl php70-pecl-zip php70-opcache

RUN yum -y install python-pip
RUN python-pip install awscli

RUN wget -O /usr/local/bin/composer https://getcomposer.org/composer.phar
RUN chmod +x /usr/local/bin/composer

RUN composer global require "phpunit/phpunit=^5.0"
RUN composer global require phpmd/phpmd
RUN composer global require squizlabs/php_codesniffer
RUN composer global require sebastian/phpcpd
ENV PATH="/root/.composer/vendor/bin:${PATH}"

RUN wget -O /usr/local/bin/codecept http://codeception.com/codecept.phar
RUN chmod a+x /usr/local/bin/codecept
