FROM bfren/nginx-php:php7.4-2.2.21

ENV \
    # set to the application's external URL
    FREESCOUT_URL= \
    # admin user's first name
    FREESCOUT_ADMIN_FIRSTNAME= \
    # admin user's last name
    FREESCOUT_ADMIN_LASTNAME= \
    # admin user's email address
    FREESCOUT_ADMIN_EMAIL= \
    # admin user's password
    FREESCOUT_ADMIN_PASS=

COPY ./overlay /
COPY ./FREESCOUT_REVISION /tmp/FREESCOUT_VERSION
COPY ./PHP_BUILD /tmp/PHP_VERSION

COPY ./overlay /

RUN bf-install

VOLUME [ "/data" ]
