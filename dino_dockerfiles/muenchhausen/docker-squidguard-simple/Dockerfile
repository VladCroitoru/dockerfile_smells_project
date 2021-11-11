FROM sameersbn/squid:latest
MAINTAINER derk@muenchhausen.de

RUN apt-get update \
 && apt-get install -y squidguard \ 
 && apt-get install -y apache2

RUN sudo echo 'AddType application/x-ns-proxy-autoconfig .dat' >> /etc/apache2/httpd.conf
ADD wpat.dat /var/www/html/wpat.dat
ADD block.html /var/www/html/block.html

ADD whiteUrls /var/lib/squidguard/db/WL/
ADD whiteDomains /var/lib/squidguard/db/WL/
RUN chown proxy:proxy /var/lib/squidguard/db -R 

RUN echo "redirect_program /usr/bin/squidGuard -c /etc/squidguard/squidGuard.conf" >> /etc/squid3/squid.conf

ADD squidGuard.conf /etc/squidguard/squidGuard.conf

ADD startSquidGuard /startSquidGuard
RUN sudo chmod a+x /startSquidGuard

EXPOSE 3128 80
VOLUME ["/var/spool/squid3"]

CMD ["/startSquidGuard"]
