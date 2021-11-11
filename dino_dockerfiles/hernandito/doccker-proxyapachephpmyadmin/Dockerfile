FROM phusion/baseimage:0.9.16
MAINTAINER hernando <me@seandion.com>

# Set correct environment variables
ENV HOME /root
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV TERM xterm



# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Configure user nobody to match unRAID's settings
 RUN \
 usermod -u 99 nobody && \
 usermod -g 100 nobody && \
 usermod -d /home nobody && \
 chown -R nobody:users /home

# Disable SSH
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Install proxy Dependencies
RUN \
  apt-get update -q && \
  apt-get install -qy apache2 php5 mc php5-mysql libapache2-mod-php5 wget inotify-tools libapache2-mod-proxy-html && \
 # apt-get install -qy libapache2-mod-php5 wget inotify-tools php5-gd php5-sqlite php5-mcrypt php5-tidy php5-mysql libapache2-mod-proxy-html && \
  apt-get clean -y && \
  rm -rf /var/lib/apt/lists/*
  
# Enable proxy
RUN \
  a2enmod proxy proxy_http proxy_ajp rewrite deflate substitute headers proxy_balancer proxy_connect proxy_html ssl xml2enc 
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

ADD apache2.conf /etc/apache2/apache2.conf
ADD ports.conf /etc/apache2/ports.conf

# Manually set the apache environment variables in order to get apache to work immediately.
RUN \
echo www-data > /etc/container_environment/APACHE_RUN_USER && \
echo www-data > /etc/container_environment/APACHE_RUN_GROUP && \
echo /var/log/apache2 > /etc/container_environment/APACHE_LOG_DIR && \
echo /var/lock/apache2 > /etc/container_environment/APACHE_LOCK_DIR && \
echo /var/run/apache2.pid > /etc/container_environment/APACHE_PID_FILE && \
echo /var/run/apache2 > /etc/container_environment/APACHE_RUN_DIR

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
