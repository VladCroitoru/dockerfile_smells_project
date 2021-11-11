FROM ubuntu:14.04.4

MAINTAINER John Hudson  <john@jehudson.me>

RUN apt-get -y update
RUN apt-get -y upgrade

# Install apache, PHP, and supplimentary programs. curl and lynx-cur are for debugging the container.
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 libapache2-mod-php5 php5-mysql php5-gd php-pear php-apc php5-curl curl lynx-cur libapache2-mod-proxy-html libxml2-dev
# Enable apache mods.
RUN a2enmod php5
RUN a2enmod rewrite
RUN a2enmod proxy
RUN a2enmod proxy_http
RUN a2enmod proxy_ajp
RUN a2enmod rewrite
RUN a2enmod deflate
RUN a2enmod headers
RUN a2enmod proxy_balancer
RUN a2enmod proxy_connect
RUN a2enmod proxy_html


# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

EXPOSE 80 443 3015

# Update the default apache site with the config we created.
ADD apache-config.conf /etc/apache2/sites-available/000-default.conf
ADD gallery.gonad.org.uk.conf /etc/apache2/sites-available/
ADD gonad.org.uk.conf /etc/apache2/sites-available/
ADD vocalissimo.org.conf /etc/apache2/sites-available/
ADD notpavarotti.org.uk.conf /etc/apache2/sites-available/
ADD notpavarotti.co.uk.conf /etc/apache2/sites-available/
ADD linuxprofessionals.co.uk.conf /etc/apache2/sites-available/
ADD vocalissimo.co.uk.conf /etc/apache2/sites-available/
ADD jehudson.me.conf /etc/apache2/sites-available
ADD bigband.gonad.org.uk.conf /etc/apache2/sites-available
ADD weather.gonad.org.uk.conf /etc/apache2/sites-available
RUN a2ensite 000-default.conf
RUN a2ensite gonad.org.uk.conf
RUN a2ensite gallery.gonad.org.uk.conf
RUN a2ensite vocalissimo.org.conf
RUN a2ensite notpavarotti.org.uk.conf
RUN a2ensite notpavarotti.co.uk.conf
RUN a2ensite linuxprofessionals.co.uk.conf
RUN a2ensite vocalissimo.co.uk.conf
RUN a2ensite jehudson.me.conf
RUN a2ensite bigband.gonad.org.uk.conf
RUN a2ensite weather.gonad.org.uk.conf

# By default, simply start apache.
CMD /usr/sbin/apache2ctl -D FOREGROUND
