FROM centos:7

MAINTAINER Alfredo Peña Alonso <alfredopenaalonso@gmail.com>

# Update packages
RUN yum -y update

# Install EPEL
RUN yum install -y epel-release

# Install, configure and start Nginx
RUN echo "[nginx]" > /etc/yum.repos.d/nginx.repo
RUN echo "name=nginx repo" >> /etc/yum.repos.d/nginx.repo
RUN echo "baseurl=http://nginx.org/packages/centos/7/\$basearch" >> /etc/yum.repos.d/nginx.repo
RUN echo "gpgcheck=0" >> /etc/yum.repos.d/nginx.repo
RUN echo "enabled=1" >> /etc/yum.repos.d/nginx.repo
RUN yum install -y nginx-1.12.1

# Install and start MariaDB
RUN echo "[mariadb]" > /etc/yum.repos.d/mariadb.repo
RUN echo "name = MariaDB" >> /etc/yum.repos.d/mariadb.repo
RUN echo "baseurl = http://yum.mariadb.org/10.2/centos7-amd64" >> /etc/yum.repos.d/mariadb.repo
RUN echo "gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB" >> /etc/yum.repos.d/mariadb.repo
RUN echo "gpgcheck=1" >> /etc/yum.repos.d/mariadb.repo
RUN yum install -y MariaDB-server MariaDB-client

# Install, configure and start PHP-FPM and XDebug
RUN yum install -y http://rpms.remirepo.net/enterprise/remi-release-7.rpm
RUN yum install -y --enablerepo=remi --enablerepo=remi-php71 php-fpm php-mysql php-mbstring php-devel php-pear
RUN yum install -y gcc gcc-c++ autoconf automake
RUN pecl install Xdebug
RUN sed -i '/^;cgi.fix_pathinfo=1$/c\cgi.fix_pathinfo=0' /etc/php.ini
RUN sed -i '/^user\s=\sapache$/c\user = nginx' /etc/php-fpm.d/www.conf
RUN sed -i '/^group\s=\sapache$/c\group = nginx' /etc/php-fpm.d/www.conf

EXPOSE 80 443 3306
