FROM centos:centos6

RUN yum install -y mysql mysql-server php php-mysql php-pdo php-gd php-mbstring php-bcmath httpd tar

RUN curl -L -o RackTables-latest.tar.gz 'http://sourceforge.net/projects/racktables/files/latest/download?source=files'
RUN tar xzf RackTables-latest.tar.gz
RUN cd $(find -type d -name 'RackTables-*') && rmdir /var/www/html && cp -a wwwroot /var/www/html
RUN touch /var/www/html/inc/secret.php && chmod 666 /var/www/html/inc/secret.php

ADD init.sql /usr/local/share/racktables/init.sql
RUN service mysqld start && cat /usr/local/share/racktables/init.sql | mysql -u root
ADD chsecret.sh /usr/local/share/racktables/chsecret.sh
RUN chmod +x /usr/local/share/racktables/chsecret.sh

ADD start.sh /usr/local/bin/start
RUN chmod +x /usr/local/bin/start
ADD stop.sh /usr/local/bin/stop
RUN chmod +x /usr/local/bin/stop

EXPOSE 80

CMD /usr/local/bin/start && tail -F /var/log/httpd/*
