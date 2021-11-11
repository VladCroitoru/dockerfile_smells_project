### CentOS Imageのダウンロード
FROM centos:centos6
### httpdのインストール、監視対象PHPファイルのアップロード##
RUN yum -y install httpd php
ADD docker-newrelic-php/index.php /var/www/html
### New Relic APM Agentのインストールおよびライセンスキーの設定
RUN rpm -Uvh http://yum.newrelic.com/pub/newrelic/el5/x86_64/newrelic-repo-5-3.noarch.rpm
RUN yum -y install newrelic-php5
RUN newrelic-install install
RUN sed -E -i 's/REPLACE_WITH_REAL_KEY/"d859c7f560872148038a0fb2913bc1eb1b5f309a"/' /etc/php.d/newrelic.ini
### httpdの起動
CMD ["/usr/sbin/httpd", "-DFOREGROUND"]