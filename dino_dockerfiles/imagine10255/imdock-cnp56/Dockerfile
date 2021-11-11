FROM centos:centos6
MAINTAINER Imagine Chiu<imagine10255@gmail.com>

ENV SSH_PASSWORD=P@ssw0rd

# Setting DateTime Zone
RUN cp -p /usr/share/zoneinfo/Asia/Taipei /etc/localtime

# Install base tool
RUN yum -y install vim wget tar
RUN yum -y groupinstall development

# Install PHP56-FPM (https://webtatic.com/packages/php56)
RUN rpm --import http://ftp.riken.jp/Linux/fedora/epel/RPM-GPG-KEY-EPEL-6 && \
    rpm -Uvh https://mirror.webtatic.com/yum/el6/latest.rpm
RUN yum -y install php56w php56w-fpm php56w-mbstring php56w-xml php56w-mysql php56w-pdo php56w-gd php56w-pecl-imagick php56w-opcache php56w-pecl-memcache php56w-intl php56w-pecl-xdebug

# Install php-mssql,mcrypt
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
RUN yum -y install php56w-mssql php56w-mcrypt

# Install Nginx
RUN rpm --import http://ftp.riken.jp/Linux/fedora/epel/RPM-GPG-KEY-EPEL-6 && \
    rpm -ivh http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm && \
    yum -y update nginx-release-centos && \
    cp -p /etc/yum.repos.d/nginx.repo /etc/yum.repos.d/nginx.repo.backup && \
    sed -i -e "s/enabled=1/enabled=0/g" /etc/yum.repos.d/nginx.repo
RUN yum -y --enablerepo=nginx install nginx

# Ensure that PHP5 FPM is run as root.
RUN sed -i -e 's/user = apache/user = nginx/' /etc/php-fpm.d/www.conf
RUN sed -i -e 's/group = apache/group = nginx/' /etc/php-fpm.d/www.conf
RUN mv /etc/php.d/xdebug.ini /etc/php.d/xdebug.ini.disable


# Setting Composer
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer && \
    echo 'export PATH="/root/.composer/vendor/bin:$PATH"' >> /root/.bashrc

# Install Supervisor
RUN yum -y install supervisor

# Install crontab service
RUN yum -y install vixie-cron crontabs
RUN sed -ie '/pam_loginuid/d' /etc/pam.d/crond


# Install SSH Service
RUN yum install -y openssh-server passwd
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config && \
    echo "${SSH_PASSWORD}" | passwd "root" --stdin && \
    ssh-keygen -q -t rsa -N '' -f /etc/ssh/ssh_host_rsa_key && \
    ssh-keygen -q -t dsa -N '' -f  /etc/ssh/ssh_host_dsa_key && \
    ssh-keygen -q -t ecdsa -N '' -f /etc/ssh/ssh_host_ecdsa_key


# Delete Install data-info
RUN yum clean all && rm -f /var/log/yum.log


# Add configuration files
COPY conf/nginx.conf /etc/nginx/
COPY conf/supervisord.conf /etc/supervisor/supervisord.conf
COPY conf/www.conf /etc/php-fpm.d/www.conf
COPY sites-module /etc/nginx/sites-module


VOLUME ["/var/www", "/etc/nginx/conf.d"]

EXPOSE 22 80 443 9000

# Executing supervisord
# -n / --nodaemon : runs in foreground ( required for docker )
# -c <configfile> : specifies the config file
ENTRYPOINT /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf