
FROM tutum/apache-php

RUN apt-get update -yq
RUN apt-get upgrade -yq

ADD . /var/webservices/3d-map-tiles

ADD tools/apache2.conf /etc/apache2/conf-available/webservices.conf
RUN a2enconf webservices

RUN a2enmod rewrite
RUN a2enmod headers

ADD config.json.sample /var/webservices/3d-map-tiles/config.json

RUN rm -fr /app
ADD example /app/example
RUN echo "<?php header('Location: /example/'); ?>" >> /app/index.php

