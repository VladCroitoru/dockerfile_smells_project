FROM centos/httpd:latest
MAINTAINER dayreiner

RUN yum clean all && yum makecache fast && yum -y update \
    && yum -y install https://mirror.webtatic.com/yum/el7/webtatic-release.rpm && yum -y update \
    && yum -y install git composer php56w php56w-cli php-56w-common php56w-opcache php56w-mysql php56w-mbstring php56w-xml php56w-gd php56w-pear php56w-intl \
    && yum -y install php-drush-drush postfix tcping which && yum clean all

RUN echo "Setting up SSH for GitHub Checkouts..." \
    && mkdir -p /root/.ssh && chmod 700 /root/.ssh \
    && touch /root/.ssh/known_hosts \
    && ssh-keyscan -H github.com >> /root/.ssh/known_hosts \
    && chmod 600 /root/.ssh/known_hosts \
    && echo "Setting up postfix and phpmail for outbound email.." \
    && touch /var/log/phpmail.log \
    && mkfifo /var/spool/postfix/public/pickup \
    && chown apache: /var/www/html

# Setup htaccess and apache conf
COPY config/main.cf /etc/postfix/main.cf
COPY config/php.ini /etc/php.ini

EXPOSE 80
ENTRYPOINT ["/usr/sbin/httpd"]
CMD ["-DFOREGROUND"]
