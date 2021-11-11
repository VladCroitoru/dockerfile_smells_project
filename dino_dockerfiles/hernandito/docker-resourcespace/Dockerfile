FROM phusion/baseimage:0.9.16
MAINTAINER hernandito

# Set correct environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV HOME            /root
ENV LC_ALL          C.UTF-8
ENV LANG            en_US.UTF-8
ENV LANGUAGE        en_US.UTF-8
ENV TERM xterm


# Use baseimage-docker's init system
CMD ["/sbin/my_init"]


# Configure user nobody to match unRAID's settings
 RUN \
 usermod -u 99 nobody && \
 usermod -g 100 nobody && \
 usermod -d /home nobody && \
 chown -R nobody:users /home

RUN add-apt-repository ppa:mc3man/trusty-media
RUN apt-get update 
RUN apt-get install -qy mc
RUN apt-get install -qy tmux
RUN apt-get install -qy php5-mysql
RUN apt-get install -qy php5-mysqlnd 
RUN apt-get install -qy libimage-exiftool-perl 
RUN apt-get install -qy antiword 
RUN apt-get install -qy poppler-utils 
RUN apt-get install -qy ffmpeg 
RUN apt-get install -qy libav-tools 
RUN apt-get install -qy libavcodec-extra-54 
RUN apt-get install -qy libavformat-extra-54 
RUN apt-get install -qy libgs-dev 
RUN apt-get install -qy imagemagick 
RUN apt-get install -qy ghostscript


# Install proxy Dependencies
RUN \
  apt-get update -q && \
  apt-get install -qy apache2 php5 php5-common curl libcurl3 php5-curl libapache2-mod-php5 php-xml-parser php5-gd php5-sqlite php5-mcrypt php5-tidy php5-cli php5-mysql inotify-tools libapache2-mod-proxy-html && \
  apt-get clean -y && \
  rm -rf /var/lib/apt/lists/*
 
RUN \
  service apache2 restart && \
  rm -R -f /var/www && \
  ln -s /web /var/www
  
# Update apache configuration with this one
RUN \
  mv /etc/apache2/sites-available/000-default.conf /etc/apache2/000-default.conf && \
  rm /etc/apache2/sites-available/* && \
  rm /etc/apache2/apache2.conf && \
  ln -s /config/proxy-config.conf /etc/apache2/sites-available/000-default.conf && \
  ln -s /var/log/apache2 /logs

ADD proxy-config.conf /etc/apache2/000-default.conf
ADD apache2.conf /etc/apache2/apache2.conf
ADD ports.conf /etc/apache2/ports.conf

ADD php.ini /etc/php5/apache2/php.ini
ADD php.ini /etc/php5/cli/php.ini

# Manually set the apache environment variables in order to get apache to work immediately.
RUN \
echo www-data > /etc/container_environment/APACHE_RUN_USER && \
echo www-data > /etc/container_environment/APACHE_RUN_GROUP && \
echo /var/log/apache2 > /etc/container_environment/APACHE_LOG_DIR && \
echo /var/lock/apache2 > /etc/container_environment/APACHE_LOCK_DIR && \
echo /var/run/apache2.pid > /etc/container_environment/APACHE_PID_FILE && \
echo /var/run/apache2 > /etc/container_environment/APACHE_RUN_DIR

RUN mkdir /home/resourcespace
#RUN mkdir /home/resourcespace2

ADD resourcespace/ /home/resourcespace/
#ADD resourcespace/ /home/resourcespace2/
#RUN mv /home/resourcespace/ /web/


# Expose Ports
EXPOSE 80 443

# The www directory and proxy config location
VOLUME ["/config", "/web", "/logs"]


# Add firstrun.sh to execute during container startup
ADD firstrun.sh /etc/my_init.d/firstrun.sh
RUN chmod +x /etc/my_init.d/firstrun.sh

# Add inotify.sh to execute during container startup
RUN mkdir /etc/service/inotify
ADD inotify.sh /etc/service/inotify/run
RUN chmod +x /etc/service/inotify/run



# Add apache to runit
RUN mkdir /etc/service/apache
ADD apache-run.sh /etc/service/apache/run
RUN chmod +x /etc/service/apache/run
ADD apache-finish.sh /etc/service/apache/finish
RUN chmod +x /etc/service/apache/finish
