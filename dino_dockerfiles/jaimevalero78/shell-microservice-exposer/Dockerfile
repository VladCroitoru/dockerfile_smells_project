# Test
FROM       centos/httpd
MAINTAINER Jaime Valero <jaimevalero78@yahoo.es>
LABEL      Description="Generic container to receives POST http request to a shell script" Version="0.5"

# Install packages
RUN yum install -y mysql git wget
RUN curl -L https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux32 > /usr/local/bin/jq && chmod +x /usr/local/bin/jq 



# Prepare environment
RUN mkdir -p        /root/scripts/shell-microservice-exposer
ADD .               /root/scripts/shell-microservice-exposer
ADD _executor.sh     /var/www/cgi-bin/

# Permissions
RUN chmod +x -R     /root/scripts/shell-microservice-exposer/

# Apache
RUN sed -i 's/Options None/Options FollowSymLinks Indexes/g' /etc/httpd/conf/httpd.conf
RUN httpd -T -k graceful 2>/dev/null 1>/dev/null

ENTRYPOINT ["/root/scripts/shell-microservice-exposer/entrypoint.sh"]

EXPOSE 80


