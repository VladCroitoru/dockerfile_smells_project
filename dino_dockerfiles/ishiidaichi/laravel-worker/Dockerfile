#
#--------------------------------------------------------------------------
# Image Setup
#--------------------------------------------------------------------------
#

FROM ishiidaichi/laradock-workspace-mongo:latest

MAINTAINER Daichi Ishii <me@ishiidaichi.com>

USER root

RUN add-apt-repository universe
RUN apt-get update
RUN apt-get -y install supervisor

RUN mkdir /var/log/php
RUN touch /var/log/php/horizon.log
RUN chmod -R 777 /var/log/php

COPY ./crontab /etc/cron.d
RUN chmod -R 644 /etc/cron.d

#
#--------------------------------------------------------------------------
# Optional Supervisord Configuration
#--------------------------------------------------------------------------
#
# Modify the ./supervisor.conf file to match your App's requirements.
# Make sure you rebuild your container with every change.
#

COPY supervisord.conf /etc/supervisord.conf

#
#--------------------------------------------------------------------------
# Optional Software's Installation
#--------------------------------------------------------------------------
#
# If you need to modify this image, feel free to do it right here.
#
    # -- Your awesome modifications go here -- #


#
#--------------------------------------------------------------------------
# Final Touch
#--------------------------------------------------------------------------
#

WORKDIR /var/www

CMD ["/usr/bin/supervisord", "-n", "-c",  "/etc/supervisord.conf"]
