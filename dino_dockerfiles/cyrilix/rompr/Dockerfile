FROM nginx
MAINTAINER Cyrille Nofficial<cynoffic@cyrilix.fr>

LABEL version="0.1"
LABEL description="Web frontend for MPD and Mopidy"

RUN     DEBIAN_FRONTEND=noninteractive  &&\
        apt-get update &&\
        apt-get upgrade &&\
        apt-get -y install php5-fpm php5-curl php5-sqlite imagemagick php5-json supervisor

RUN     adduser --system --home /opt/rompr rompr

ADD docker/php-fpm/php-fpm.conf /etc/php5/fpm/php-fpm.conf
ADD docker/nginx/rompr.conf /etc/nginx/conf.d/default.conf
ADD docker/supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD . /usr/share/nginx/html
RUN chown -R rompr /usr/share/nginx/html

RUN rm -r /usr/share/nginx/html/docker

EXPOSE 80

CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
