FROM centos:7

ENV ECCUBE_VERSION=3.0.16 \
    ROOTUSER=postgres \
    ROOTPASS=password \
    DBSERVER=postgres \
    DBNAME=cube3_dev \
    DBUSER=cube3_dev_user \
    DBPORT=5432 \
    DBPASS=password \
    DB_TYPE=pgsql \
    DB_CREATE=true \
    DB_INIT=true \
    MAIL_HOST=localhost \
    MAIL_PORT=25 \
    MAIL_USER=root \
    MAIL_PASS=password 

COPY . /root
COPY entrypoint.sh /entrypoint.sh

RUN cp /etc/localtime /root/old.timezone && \
    rm /etc/localtime && \
    ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    cp /root/entrypoint.sh /entrypoint.sh && \
    chmod +x /entrypoint.sh && \
    rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 && \
    yum -y update && \
    yum install -y php php-pdo php-mysql php-pdo_pgsql php-dom php-mbstring php-gd php-xml php-fpm php-soap && \
    yum install -y epel-release && \
    rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7  && \
    yum install -y php-mcrypt php-apc nginx && \
    yum clean all && \
    rm -rf /var/cache/yum && \
    cp -f /root/www.conf /etc/php-fpm.d/www.conf && \
    cp -f /root/nginx.conf /etc/nginx/nginx.conf && \
    cp -f /root/php.ini /etc/php.ini && \
    mv /root/certificates /certificates && \
    rm -rf /root/* && \
    curl -Ss -o eccube.tar.gz https://codeload.github.com/EC-CUBE/ec-cube/tar.gz/$ECCUBE_VERSION && \
    tar -zxvf eccube.tar.gz -C / && \
    rm eccube.tar.gz && \
    mv /ec-cube-$ECCUBE_VERSION /ec-cube && \
    cd /ec-cube && \
    curl -Ss -o composer-setup.php https://getcomposer.org/installer && \
    php composer-setup.php && \
    mv composer.phar /usr/bin/composer && \
    composer install && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log
    # php eccube_install.php pgsql
    
VOLUME /ec-cube
WORKDIR /ec-cube

EXPOSE 80 443

ENTRYPOINT ["/entrypoint.sh"]

# yum install cifs-utils