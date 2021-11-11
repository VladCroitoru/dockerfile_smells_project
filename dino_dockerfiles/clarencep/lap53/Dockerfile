FROM centos:6

RUN yum install -y httpd \
    && rm -f /var/www/html/index.html \
    && echo '<?php phpinfo();' > /var/www/html/index.php \
    && yum install -y gcc make libXpm.so.4 libt1.so.5 autoconf automake gd \
    && yum install -y openssl openssl-devel readline readline-devel \
    && yum install -y openssl098e compat-readline5 compat-openldap \
    && yum install -y libxslt \
    && yum install -y mysql-devel \
    && yum install -y php php-cli php-devel php-gd php-xml php-intl php-mysql php-pdo \
    && yum remove -y gcc autoconf automake \
    && yum clean all \
    && find /var/log -type f -print0 | xargs -0 rm -rf /tmp/*
    
RUN sed 's|logs/access_log|/dev/stdout|' -i.bak /etc/httpd/conf/httpd.conf \
    && sed 's|logs/error_log|/dev/stderr|' -i.bak /etc/httpd/conf/httpd.conf
    
CMD [ "/usr/sbin/httpd", "-DFOREGROUND" ]

EXPOSE 80
