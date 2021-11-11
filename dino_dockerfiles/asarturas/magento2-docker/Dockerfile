FROM centos:centos6

# Install required packages

RUN yum -y install wget \
    curl unzip supervisor g++ make mc vim tar gcc pcre-devel openssl-devel patch libmcrypt-devel \
        libxml2-devel bzip2-devel libcurl-devel readline-devel git && \
    yum -y update && \
    yum -y install https://mirror.webtatic.com/yum/el6/latest.rpm && \
    yum -y install php56w-pecl-memcache php56w-fpm php56w-intl php56w-mcrypt php56w-mbstring \
        php56w-mysql php56w-pdo php56w-mbstring php56w-soap php56w-pecl-zendopcache php56w-xml \
        php56w-gd php56w-opcache php56w-pecl-imagick && \
    rpm -Uvh http://dev.mysql.com/get/mysql-community-release-el6-5.noarch.rpm && \
    yum -y install mysql-community-server && \
    wget http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm && \
    rpm -ivh nginx-release-centos-6-0.el6.ngx.noarch.rpm && \
    yum -y install nginx && \
    yum -y upgrade ca-certificates && \
    yum -y install https://repo.varnish-cache.org/redhat/varnish-4.0.el6.rpm && \
    yum -y install epel-release && \
    yum -y install varnish && \
    curl -sS https://getcomposer.org/installer | \
        php -- --install-dir=/usr/local/bin --filename=composer

# Configure

ADD . /magento2-docker
RUN mkdir -p /etc/nginx/conf && \
    cp /magento2-docker/etc/nginx.conf/fastcgi_params.conf /etc/nginx/conf/fastcgi_params.conf && \
    cp /magento2-docker/etc/nginx.conf/magento.conf /etc/nginx/conf/magento.conf && \
    mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.default && \
    cp /magento2-docker/etc/nginx.conf/default.conf /etc/nginx/conf.d/default.conf && \
    cp /magento2-docker/etc/php.conf/php.ini /etc/php.ini && \
    mv /etc/php-fpm.d/www.conf /etc/php-fpm.d/www.conf.default && \
    cp /magento2-docker/etc/php-fpm.conf/www.conf /etc/php-fpm.d/www.conf && \
    mkdir -p /var/lib/php/session && \
    mkdir -p /var/lib/php/wsdlcache && \
    chmod -R 777 /var/lib/php/session && \
    chmod -R 777 /var/lib/php/wsdlcache && \
    mv /etc/sysconfig/varnish /etc/sysconfig/default.varnish && \
    cp /magento2-docker/etc/varnish.conf/varnish /etc/sysconfig/varnish && \
    mkdir -p /etc/varnish && \
    cp /magento2-docker/etc/varnish.conf/default.vcl /etc/varnish/default.vcl && \
    chmod +x -R /magento2-docker/scripts && \
    mkdir -p /var/www/app/magento2.docker.loc/magento2 && \
    chown -R nginx:nginx /var/www/app/magento2.docker.loc/magento2 && \
    usermod -u 1000 nginx

EXPOSE 80
VOLUME ["/var/www/app/magento2.docker.loc/magento2"]
WORKDIR /var/www/app/magento2.docker.loc/magento2
ENTRYPOINT /magento2-docker/scripts/run.sh
