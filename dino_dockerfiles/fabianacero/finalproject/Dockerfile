FROM webdevops/php-nginx:centos-7
MAINTAINER Fabian Acero Garcia <acero01@gmail.com>
LABEL NGINX con PGSQL

# Creando vhost
# Specify only the domain's name
ENV DOMAIN_NAME	fabianacero
RUN mkdir -p /etc/nginx/sites-available; mkdir -p /etc/nginx/sites-enabled
#ADD vhost.conf /etc/nginx/sites-available/$DOMAIN_NAME.conf
ADD vhost.conf /etc/nginx/sites-available/default.conf
RUN cat /etc/nginx/sites-available/default.conf | sed s/{DNAME}/$DOMAIN_NAME/g > /etc/nginx/sites-available/$DOMAIN_NAME.conf
RUN ln -sf /etc/nginx/sites-available/$DOMAIN_NAME.conf /etc/nginx/sites-enabled/$DOMAIN_NAME.conf
RUN cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bkp
RUN cat /etc/nginx/nginx.conf.bkp | sed 's/\/etc\/nginx\/conf\.d\/\*\.conf;/\/etc\/nginx\/conf\.d\/\*\.conf;\ninclude\t\/etc\/nginx\/sites-enabled\/\*\.conf;\n    server_names_hash_bucket_size 64;/g' > /etc/nginx/nginx.conf

# Configurando postgres
ENV PG_PASSWD=C4mbi0
RUN yum install php-pgsql -y
ADD index.php /app/index.php
ADD index.php  /usr/share/nginx/html/index.php