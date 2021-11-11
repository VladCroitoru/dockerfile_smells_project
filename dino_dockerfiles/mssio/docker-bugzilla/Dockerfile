FROM ubuntu:14.04.3
MAINTAINER Mario <mario@mss.io>

# Install packages
RUN apt-get update && apt-get -y install git apache2 libappconfig-perl libdate-calc-perl libtemplate-perl libmime-perl build-essential libdatetime-timezone-perl libdatetime-perl libemail-sender-perl libemail-mime-perl libemail-mime-modifier-perl libdbi-perl libdbd-mysql-perl libcgi-pm-perl libmath-random-isaac-perl libmath-random-isaac-xs-perl apache2-mpm-prefork libapache2-mod-perl2 libapache2-mod-perl2-dev libchart-perl libxml-perl libxml-twig-perl perlmagick libgd-graph-perl libtemplate-plugin-gd-perl libsoap-lite-perl libhtml-scrubber-perl libjson-rpc-perl libdaemon-generic-perl libtheschwartz-perl libtest-taint-perl libauthen-radius-perl libfile-slurp-perl libencode-detect-perl libmodule-build-perl libnet-ldap-perl libauthen-sasl-perl libtemplate-perl-doc libfile-mimeinfo-perl libhtml-formattext-withlinks-perl libfile-which-perl libgd-dev libmysqlclient-dev lynx-cur graphviz python-sphinx rst2pdf

# Bugzilla configuration
VOLUME /var/www/bugzilla
WORKDIR /usr/src/bugzilla
RUN git clone --branch release-4.4.11 https://git.mozilla.org/bugzilla/bugzilla /usr/src/bugzilla
ADD localconfig /usr/src/bugzilla/localconfig

# Apache configuration
ADD bugzilla.conf /etc/apache2/sites-available/001-bugzilla.conf
RUN a2dissite 000-default
RUN a2ensite 001-bugzilla
RUN a2enmod cgi headers expires

# Cleanup
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Run the app
EXPOSE 80
COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
