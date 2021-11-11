FROM debian:latest
MAINTAINER Christian Ashby <docker@cashby.me.uk>
# Install OS package prerequisites and configure apache
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y apache2 python python-psutil wget build-essential cron rsyslog git && \
    mkdir /var/lock/apache2 && \
    a2enmod cgi && \
    a2enmod rewrite && \
    echo "ServerName web_get_iplayer" >> /etc/apache2/sites-enabled/000-default.conf
RUN apt-get update && \
    apt-get install -y ffmpeg rtmpdump 
COPY ts-to-mp4.sh /usr/local/bin
RUN chmod +x /usr/local/bin/ts-to-mp4.sh
# Install development prerequisites
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libssl-dev libhtml-parser-perl libhttp-cookies-perl libwww-perl libxml-simple-perl libxml-libxml-perl
# Install the get_iplayer script and run it to ensure we have the appropriate cache set up in our ~
WORKDIR /usr/lib/cgi-bin
RUN wget https://raw.githubusercontent.com/get-iplayer/get_iplayer/master/get_iplayer && \
    chmod +x get_iplayer
# Install the web_get_iplayer script
COPY web_get_iplayer.py .
RUN chmod +x web_get_iplayer.py
# Configure the crontab entries for web_get_iplayer
COPY web_get_iplayer.cron.sh .
RUN chmod +x web_get_iplayer.cron.sh
COPY _etc_cron.d_web_get_iplayer /etc/cron.d/web_get_iplayer 
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
RUN chmod g-w /etc/cron.d/web_get_iplayer
# Configure web_get_iplayer
WORKDIR /var/lib
RUN mkdir web_get_iplayer
WORKDIR /var/lib/web_get_iplayer
COPY web_get_iplayer.settings .
RUN chgrp 33 . && chmod g+ws . && \
    chgrp 33 web_get_iplayer.settings && chmod g+w web_get_iplayer.settings && \
    touch /var/www/.swfinfo && chown 33:33 /var/www/.swfinfo && chmod g+w /var/www/.swfinfo && \
    mkdir /var/www/.get_iplayer && chgrp 33 /var/www/.get_iplayer && chmod g+ws /var/www/.get_iplayer && \
    chown 33:33 /var/www && \
    ln -s `which rtmpdump` /usr/lib/cgi-bin/rtmpdump
# Fix for https://stackoverflow.com/questions/29424132/error-accessing-cgi-script-inside-docker-container-operation-not-permitted-cou
RUN mkdir -p /var/run/apache2/cgisock
# Fix cron issue (see http://stackoverflow.com/questions/21926465/issues-running-cron-in-docker-on-different-hosts)
RUN cat /etc/pam.d/cron | grep -v pam_loginuid.so > /etc/pam.d/cron2 && mv /etc/pam.d/cron2 /etc/pam.d/cron
# And do some clean-up
CMD ["-m", "128"]
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_LOCK_DIR /var/lock/apache2

EXPOSE 80
VOLUME /home/iplayer

USER 0
CMD service rsyslog start && service cron start && /usr/sbin/apache2 -DFOREGROUND

