FROM bliss/hosted-whmcs

RUN curl -O http://repo.cloudlinux.com/kuberdock/whmcs-kuberdock-plugin-latest.zip
RUN unzip whmcs-kuberdock-plugin-latest.zip deploy.php

RUN php deploy.php --local=/var/opt/whmcs/whmcs-kuberdock-plugin-latest.zip \
            --kd_ip=${KD_IP} \
            --kd_login=${KD_LOGIN} \
            --kd_password=${KD_PASSWORD}

RUN chmod -R g-w /var/opt/whmcs/.*
RUN chown -R www-data:www-data /var/opt/whmcs/.*

COPY scripts/kdactivate.php /var/opt/whmcs
RUN php /var/opt/whmcs/kdactivate.php
RUN rm -f /var/opt/whmcs/kdactivate.php


