FROM debian:wheezy

RUN apt-get update && apt-get install -y apache2 apache2-utils && apt-get clean
COPY default /etc/apache2/sites-available/

EXPOSE 80

RUN mkdir /exec

RUN touch /exec/run.sh && chmod +x /exec/run.sh 
RUN echo '#!/bin/bash' >> /exec/run.sh 
RUN echo 'sed -i "s@URL@$URL@g" /etc/apache2/sites-available/default' >>  /exec/run.sh
RUN echo 'tc qdisc add dev eth0 root netem delay 250ms' >> /exec/run.sh
RUN echo 'source /etc/apache2/envvars' >> /exec/run.sh 
RUN echo 'exec apache2 -D FOREGROUND' >> /exec/run.sh 

RUN a2enmod proxy_http

CMD /exec/run.sh

