FROM ubuntu:trusty
MAINTAINER Filipe Roque <froque@premium-minds.com>

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y  apache2 libappconfig-perl libdate-calc-perl libtemplate-perl libmime-perl build-essential libdatetime-timezone-perl libdatetime-perl libemail-sender-perl libemail-mime-perl libemail-mime-modifier-perl libdbi-perl libdbd-mysql-perl libcgi-pm-perl libmath-random-isaac-perl libmath-random-isaac-xs-perl apache2-mpm-prefork libapache2-mod-perl2 libapache2-mod-perl2-dev libchart-perl libxml-perl libxml-twig-perl perlmagick libgd-graph-perl libtemplate-plugin-gd-perl libsoap-lite-perl libhtml-scrubber-perl libjson-rpc-perl libdaemon-generic-perl libtheschwartz-perl libtest-taint-perl libauthen-radius-perl libfile-slurp-perl libencode-detect-perl libmodule-build-perl libnet-ldap-perl libauthen-sasl-perl libtemplate-perl-doc libfile-mimeinfo-perl libhtml-formattext-withlinks-perl libfile-which-perl libgd-dev libmysqlclient-dev lynx-cur graphviz python-sphinx rst2pdf  && rm -rf /var/lib/apt/lists/* 

# Remove DEFAULT apache site
RUN rm -rf /var/www/html

# Make Bugzilla install Directory
ADD https://ftp.mozilla.org/pub/mozilla.org/webtools/bugzilla-4.4.8.tar.gz /tmp/
RUN tar -xvf /tmp/bugzilla-4.4.8.tar.gz -C /var/www/
RUN ln -s /var/www/bugzilla-4.4.8 /var/www/html
ADD bugzilla.conf /etc/apache2/sites-available/
WORKDIR /var/www/html
ADD checksetup_answers.txt /var/www/html
ADD params data/params

RUN /usr/bin/perl install-module.pl --all


RUN ./checksetup.pl

# Enable CGI and Disable default apache site
RUN a2enmod cgi headers expires && a2ensite bugzilla && a2dissite 000-default

# Add the start script
ADD start /opt/

# Run start script
CMD ["/opt/start"]

# Expose web server port
EXPOSE 80
