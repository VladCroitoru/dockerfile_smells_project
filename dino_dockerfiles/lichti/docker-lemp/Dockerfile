FROM debian:latest
MAINTAINER "Gustavo Lichti <gustavo@lichti.com.br>"

ENV DEBIAN_FRONTEND noninteractive

# Upgrade 
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Tools
RUN apt-get update && \
    apt-get install -y wget curl vim less && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# php-fpm
RUN apt-get update && \
    apt-get install -y php5-fpm php5-cli php5-gd php5-mcrypt php5-mysql php5-curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN sed -i 's/^listen\s*=.*$/listen = 127.0.0.1:9000/' /etc/php5/fpm/pool.d/www.conf && \
    sed -i 's/^\;error_log\s*=\s*syslog\s*$/error_log = \/var\/log\/php5\/cgi.log/' /etc/php5/fpm/php.ini && \
    sed -i 's/^\;error_log\s*=\s*syslog\s*$/error_log = \/var\/log\/php5\/cli.log/' /etc/php5/cli/php.ini && \
    mkdir /var/log/php5/ && \
    touch /var/log/php5/cli.log /var/log/php5/cgi.log && \
    chown www-data:www-data /var/log/php5/cgi.log /var/log/php5/cli.log

# nginx
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN unlink /etc/nginx/sites-enabled/default
ADD nginx/default /etc/nginx/sites-enabled/default
RUN mkdir /var/www/
ADD nginx/index.php /var/www/
RUN chown -R www-data:www-data /var/www/

# mysql
RUN apt-get update && \
    echo "mysql-server mysql-server/root_password password" | debconf-set-selections && \
    echo "mysql-server mysql-server/root_password_again password" | debconf-set-selections && \
    apt-get install -y mysql-server && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN sed -i 's/^key_buffer\s*=/key_buffer_size =/' /etc/mysql/my.cnf
RUN chown -R mysql:mysql /var/lib/mysql

#SSHD
RUN apt-get update && \ 
    apt-get install -y openssh-client openssh-server && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN mkdir /var/run/sshd
RUN echo 'root:root' |chpasswd
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

# PHPMyAdmin
ENV VERSION 4.4.3
RUN mkdir -p /var/www/phpmyadmin && \
    cd /var/www/phpmyadmin && \
    wget -O - "http://www.sourceforge.net/projects/phpmyadmin/files/phpMyAdmin/${VERSION}/phpMyAdmin-${VERSION}-all-languages.tar.gz/download" | tar --strip-components=1 -x -z && \
    rm -rf *.md .coveralls.yml ChangeLog composer.json config.sample.inc.php DCO doc examples phpunit.* README RELEASE-DATE-* setup
ADD nginx/config.inc.php /var/www/phpmyadmin/

# supervisor
## Install supervisor
RUN apt-get update && \
    apt-get install -y supervisor && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
ADD supervisor/php5-fpm.conf /etc/supervisor/conf.d/php5-fpm.conf
ADD supervisor/nginx.conf /etc/supervisor/conf.d/nginx.conf
ADD supervisor/mysql.conf /etc/supervisor/conf.d/mysql.conf
ADD supervisor/sshd.conf /etc/supervisor/conf.d/sshd.conf

WORKDIR /var/www/


EXPOSE 80
EXPOSE 22

CMD ["/usr/bin/supervisord", "--nodaemon", "-c", "/etc/supervisor/supervisord.conf"]
