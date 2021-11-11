FROM ubuntu:16.04

# Install base package
RUN apt-get -y update && apt-get install -y fortunes \
	&& apt-get install -y apache2 \
		build-essential git nginx nodejs npm mysql-client vim netcat-openbsd \
      		php7.0 php7.0-fpm php-pear php7.0-json php7.0-mysql php7.0-sybase \
		php7.0-intl php7.0-curl php7.0-zip php7.0-soap php7.0-mbstring php7.0-mcrypt php-ssh2 \
      		python2.7 python-pip python-virtualenv python-numpy python-scipy \
		python-mysqldb python-yaml \
		composer

# Download source code
RUN cd /var/www/html/ && \
    git clone https://github.com/zhukangfeng/yoursave.git && \
    cd yoursave && cp .env.example .env && composer install
