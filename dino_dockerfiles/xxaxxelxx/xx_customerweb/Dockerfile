FROM debian:jessie
MAINTAINER xxaxxelxx <x@axxel.net>

#RUN sed -e 's/$/ contrib non-free/' -i /etc/apt/sources.list 

RUN apt-get -qq -y update
#RUN apt-get -qq -y dist-upgrade

ENV TERM=xterm

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -qqy mc sqlite
RUN apt-get install -qqy php5-sqlite
RUN apt-get install -qqy php5-cgi
RUN apt-get install -qqy lighttpd

# clean up
RUN apt-get clean

COPY lighttpd.conf /etc/lighttpd/lighttpd.conf
COPY *.php /
COPY *.html /
#COPY lighttpd-plain.user /etc/lighttpd/
#RUN chown -R www-data /etc/lighttpd
#RUN chown -R www-data /var/www/html

COPY entrypoint.sh /entrypoint.sh
#COPY index.html /index.html
#COPY index.php /index.php


#ENV UPDATEPASSWORD="my-_-password"

#EXPOSE 80

ENTRYPOINT [ "/entrypoint.sh" ]
#CMD [ "bash" ]
