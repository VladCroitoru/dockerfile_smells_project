FROM alpine:3.6

RUN apk --update add apache2 php5-apache2

RUN echo "<?php phpinfo(); ?>" > /var/www/localhost/htdocs/index.php

EXPOSE 80
