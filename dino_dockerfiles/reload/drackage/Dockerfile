FROM reload/drupal-apache-ssl

COPY . /var/www/html/
COPY ./docker/init.sh /etc/my_init.d/
COPY ./sites/default/docker.settings.php /var/www/html//sites/default/settings.php

# Generate new hash_salt
RUN dd 2>/dev/null if=/dev/urandom bs=1 count=55 |  base64 >/etc/drupal-hash-salt

