FROM drupal:8.2.6-apache
MAINTAINER pierre.carre78@gmail.com

RUN sed -i "s/\(Listen 80\)/\180/" /etc/apache2/ports.conf &&\
  sed -i "s/\(.*80\)/\180/" /etc/apache2/sites-enabled/000-default.conf

RUN cp /var/www/html/sites/default/default.settings.php /var/www/html/sites/default/settings.php &&\
  chmod a+w /var/www/html/sites/default/settings.php

RUN chgrp -R 0 /var/run/apache2 &&\
  chmod -R g+rw /var/run/apache2 &&\
  find /var/run/apache2 -type d -exec chmod g+x {} +
RUN chgrp -R 0 /var/log/apache2 &&\
  chmod -R g+rw /var/log/apache2 &&\
  find /var/log/apache2 -type d -exec chmod g+x {} +
RUN chgrp -R 0 /var/lock/apache2 &&\
  chmod -R g+rw /var/lock/apache2 &&\
  find /var/lock/apache2 -type d -exec chmod g+x {} +
RUN chgrp -R 0 /var/www/html &&\
  chmod -R g+rw /var/www/html &&\
  find /var/www/html -type d -exec chmod g+x {} +
RUN chgrp -R 0 /etc/apache2 &&\
  chmod -R g+rw /etc/apache2 &&\
  find /etc/apache2 -type d -exec chmod g+x {} +

EXPOSE 8080
