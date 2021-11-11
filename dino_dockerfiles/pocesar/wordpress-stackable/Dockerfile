FROM tutum/apache-php:latest
MAINTAINER Borja Burgos <borja@tutum.co>, Feng Honglin <hfeng@tutum.co>

ENV WORDPRESS_VER 4.3.1
ENV WP_PATH /app/blog

WORKDIR /

RUN mkdir -p ${WP_PATH}
RUN apt-get update && \
    apt-get -yq install mysql-client curl && \
    rm -rf ${WP_PATH} && \
    curl -0L http://wordpress.org/wordpress-${WORDPRESS_VER}.tar.gz | tar zxv && \
    mv /wordpress ${WP_PATH} && \
    rm -rf /var/lib/apt/lists/*

RUN sed -i "s/AllowOverride None/AllowOverride All/g" /etc/apache2/apache2.conf
RUN a2enmod rewrite
ADD wp-config.php ${WP_PATH}/wp-config.php
ADD run.sh /run.sh
RUN chmod +x /*.sh

# Expose environment variables
ENV DB_HOST **LinkMe**
ENV DB_PORT **LinkMe**
ENV DB_NAME wordpress
ENV DB_USER admin
ENV DB_PASS **ChangeMe**

EXPOSE 80
VOLUME ["${WP_PATH}/wp-content"]
CMD ["/run.sh"]
