From centos
RUN yum update -y
RUN yum install -y net-tool nano httpd php
ADD run-httpd.sh /opt/run-httpd.sh
ADD phpinfo.php /var/www/html/phpinfo.php

RUN chmod +x /opt/run-httpd.sh
EXPOSE 80
CMD ["/opt/run-httpd.sh"]
