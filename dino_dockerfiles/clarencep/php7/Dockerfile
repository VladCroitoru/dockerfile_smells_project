FROM centos:7

ENV PHP_VERSION 7.1

RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
    && rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  \
    && yum install -y mod_php71w php71w-{cli,opcache,fpm,common,gd,intl,mbstring,mcrypt,mysqlnd,pdo,soap,xml} \
    && find /var/log -type f -print0 | xargs -0 rm -rf /tmp/* \
    && yum clean all

CMD php -v && php -m
