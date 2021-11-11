#Rubedo Dockerfile public

FROM centos:latest
MAINTAINER Web

#### Mongo ####

RUN yum -y update
RUN yum install -y epel-release && yum install -y tar wget
RUN mkdir -p /var/run/mongo /var/log/mongo /var/lib/mongo

#Install Mongo
RUN wget -O mongo.tgz https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel70-3.0.0.tgz
RUN tar -xvf mongo.tgz -C /usr/local --strip-components=1 && rm -f mongo.tgz

#### Elasticsearch ####

# Install required packages
RUN yum install -y java-1.7.0-openjdk.x86_64
RUN mkdir -p /var/run/elasticsearch /var/log/elasticsearch /usr/share/elasticsearch
RUN wget -O elasticsearch.tar.gz https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.5.2.tar.gz && tar -zxvf elasticsearch.tar.gz -C /usr/share/elasticsearch --strip-components=1 && rm -f elasticsearch.tar.gz
RUN /usr/share/elasticsearch/bin/plugin install elasticsearch/elasticsearch-analysis-icu/2.5.0 \
	&& /usr/share/elasticsearch/bin/plugin install elasticsearch/elasticsearch-mapper-attachments/2.5.0

#### Apache ####

# Install PHP env
RUN yum install -y httpd git vim php php-gd php-ldap php-odbc php-pear php-xml php-xmlrpc php-mbstring php-snmp php-soap curl curl-devel gcc php-devel php-intl make openssl-devel; yum -y clean all

# Update httpd conf
RUN cp /etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf.old && \
    rm /etc/httpd/conf.d/welcome.conf -f && \
    sed -i 's#/var/www/html#/var/www/html/rubedo/public#g' /etc/httpd/conf/httpd.conf && \
    sed -i 's#Options Indexes FollowSymLinks#Options -Indexes +FollowSymLinks#g' /etc/httpd/conf/httpd.conf && \
    sed -i 's#AllowOverride None#AllowOverride All#g' /etc/httpd/conf/httpd.conf && \
    sed -i 's#ServerName www.example.com:80#ServerName www.example.com:80\nServerName localhost:80#g' /etc/httpd/conf/httpd.conf

# Install PHP Mongo extension
RUN pecl channel-update pecl.php.net
RUN pecl install mongo
ADD mongo.ini /etc/php.d/mongo.ini

# Upgrade default limits for PHP
RUN sed -i 's#memory_limit = 128M#memory_limit = 512M#g' /etc/php.ini && \
    sed -i 's#max_execution_time = 30#max_execution_time = 240#g' /etc/php.ini && \
    sed -i 's#upload_max_filesize = 2M#upload_max_filesize = 20M#g' /etc/php.ini && \
    sed -i 's#;date.timezone =#date.timezone = "Europe/Paris"\n#g' /etc/php.ini

# Expose port
EXPOSE 80
ENV URL **None**
ENV VERSION **None**
ENV GITHUB_APIKEY **None**
RUN mkdir -p /root/.ssh && \
    echo "github.com,192.30.252.131 ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ==" > /root/.ssh/known_hosts && \
    chmod 644 /root/.ssh/known_hosts

# Start script
COPY generate-composer-extension.py /generate-composer-extension.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /*.sh
ENTRYPOINT ["/entrypoint.sh"]
VOLUME /var/www/html/rubedo
CMD ["/usr/bin/tail", "-f", "/var/log/httpd/error_log"]
