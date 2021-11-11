FROM 1and1internet/ubuntu-16-apache-php-7.0:latest
MAINTAINER james.wilkins@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive
COPY files /
RUN \
    apt-get update && \
    apt-get install -y php7.0-mcrypt php7.0-intl php7.0-mbstring php7.0-gd php7.0-mysql php7.0-mcrypt php7.0-curl php7.0-intl php7.0-xsl php7.0-mbstring php7.0-zip php7.0-bcmath php7.0-iconv bzip2 && \
    #sed -i -e 's/;always_populate_raw_post_data = -1/always_populate_raw_post_data = -1/g' /etc/php/5.6/apache2/php.ini && \
    sed -i -e 's/max_execution_time = 30/max_execution_time = 18000/g' /etc/php/7.0/apache2/php.ini && \
    sed -i -e 's/memory_limit = 128M/memory_limit = 768M/g' /etc/php/7.0/apache2/php.ini && \
    cd /usr/src && curl -O http://mirror.fhpaas.fasthosts.net.uk/docker/Magento-CE-2.0.7+sample_data-2016-05-24-01-28-33.tar.bz2 && \
    rm -rf /var/lib/apt/lists/* && \
    chmod 755 /hooks /init
EXPOSE 8080
ENV MYSQL_USER=magento \
    MYSQL_PASSWORD=EnvVarHere \
    MYSQL_DATABASE=magento \
    MYSQL_HOST=mysql
