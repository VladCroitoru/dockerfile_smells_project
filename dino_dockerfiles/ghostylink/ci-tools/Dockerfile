# Dockerfile based on lamp container
FROM fauria/lamp

MAINTAINER Kevin REMY <kevanescence@hotmail.fr>

RUN apt-get update && apt-get install snmp && apt-get -y install php7.0-mbstring && \
    pecl install xdebug && \
    echo "zend_extension=$(find /usr/lib/php/ -name xdebug.so)" >> /etc/php/7.0/cli/php.ini 

ENV TESTED_CODE="/tested_code" CI_SERVER=1 CI_FROM_DOCKER=1

RUN mkdir /image /tested_code

###
EXPOSE 80

COPY . /image/

RUN chmod -R uo+x /image

CMD ["/image/launch.sh"]
