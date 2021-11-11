FROM centos:6

RUN yum install -y httpd \
    && rm -f /var/www/html/index.html \
    && echo '<?php phpinfo();' > /var/www/html/index.php \
    && rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm \
    && rpm -Uvh https://mirror.webtatic.com/yum/el6/latest.rpm \
    && yum install -y gcc make autoconf automake gd \
    && yum install -y openssl openssl-devel readline readline-devel \
    && yum install -y php56w php56w-{cli,devel,gd,xml,intl,mysql,pdo,common,pear,soap} \
    && pecl install channel://pecl.php.net/xhprof-0.9.4 \
    && echo 'extension=xhprof.so' >> /etc/php.d/xhprof.ini \
    && yum remove -y gcc autoconf automake \
    && yum clean all \
    && find /var/log -type f -print0 | xargs -0 rm -rf /tmp/*
    
RUN sed 's|logs/access_log|/dev/stdout|' -i.bak /etc/httpd/conf/httpd.conf \
    && sed 's|logs/error_log|/dev/stderr|' -i.bak /etc/httpd/conf/httpd.conf
    
CMD [ "/usr/sbin/httpd", "-DFOREGROUND" ]

EXPOSE 80
