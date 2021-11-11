FROM hoangthienan/docker-nginx-phalcon:latest

RUN apt-get update 
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y build-essential python-setuptools python-pip unzip libaio-dev

# Oracle instantclient
ADD oracle/instantclient-basic-linux.x64-12.1.0.2.0.zip /tmp/
ADD oracle/instantclient-sdk-linux.x64-12.1.0.2.0.zip /tmp/
ADD oracle/instantclient-sqlplus-linux.x64-12.1.0.2.0.zip /tmp/

RUN unzip /tmp/instantclient-basic-linux.x64-12.1.0.2.0.zip -d /usr/local/
RUN unzip /tmp/instantclient-sdk-linux.x64-12.1.0.2.0.zip -d /usr/local/
RUN unzip /tmp/instantclient-sqlplus-linux.x64-12.1.0.2.0.zip -d /usr/local/
RUN ln -s /usr/local/instantclient_12_1 /usr/local/instantclient
RUN ln -s /usr/local/instantclient/libclntsh.so.12.1 /usr/local/instantclient/libclntsh.so
RUN ln -s /usr/local/instantclient/sqlplus /usr/bin/sqlplus
RUN echo 'instantclient,/usr/local/instantclient' | pecl install oci8-2.0.11
RUN echo "extension=oci8.so" > /etc/php5/fpm/conf.d/30-oci8.ini
RUN echo "extension=oci8.so" > /etc/php5/cli/conf.d/30-oci8.ini

# Install supervisord
RUN easy_install supervisor

# install envtpl for replace
RUN pip install envtpl

# Copy startup script for getting environment information such as config...
ADD startup.sh /var/startup.sh
RUN chmod +x /var/startup.sh

# tweak php-fpm config (base on 20MB/process and 8GB Memory)
RUN sed -i -e "s/pm.max_children = 5/pm.max_children = 400/g" /etc/php5/fpm/pool.d/www.conf && \
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 8/g" /etc/php5/fpm/pool.d/www.conf && \
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 4/g" /etc/php5/fpm/pool.d/www.conf && \
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 12/g" /etc/php5/fpm/pool.d/www.conf && \
sed -i -e "s/;pm.max_requests = 500/pm.max_requests = 200/g" /etc/php5/fpm/pool.d/www.conf

# syslog-ng graylog config
ADD graylog.conf.tpl /etc/syslog-ng/conf.d/graylog.conf.tpl

# supervisord config
ADD supervisord.conf /etc/supervisord.conf

# create log directory for supervisord
RUN mkdir /var/log/supervisor/

# create conf directory for supervisord
RUN mkdir -p /etc/supervisor/conf.d/

CMD [ "/var/startup.sh" ]

RUN apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
