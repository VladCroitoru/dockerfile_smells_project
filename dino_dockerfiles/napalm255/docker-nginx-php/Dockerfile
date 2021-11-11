# Pull from the ubuntu:14.04.3 image
FROM ubuntu:14.04.3

# Update cache and install base packages
RUN apt-get update && apt-get -y install \
    software-properties-common \
    python-software-properties \
    debian-archive-keyring \
    wget \
    curl \
    vim \
    aptitude \
    dialog \
    net-tools \
    mcrypt \
    build-essential \
    git

# Download Nginx signing key
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C300EE8C

# Add to repository sources list
RUN add-apt-repository ppa:nginx/stable

# Update cache and install Nginx
RUN apt-get update && apt-get -y install \
    nginx \
    php5-fpm \
    php5-cli \
    php5-mysql \
    php5-curl \
    php5-mcrypt \
    php5-gd \
    php5-redis

# Turn off daemon mode
# Reference: http://stackoverflow.com/questions/18861300/how-to-run-nginx-within-docker-container-without-halting
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

# Backup the default configurations
RUN cp /etc/php5/fpm/php.ini /etc/php5/fpm/php.ini.original.bak
RUN mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.original

# Configure PHP settings
RUN perl -pi -e 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php5/fpm/php.ini
RUN perl -pi -e 's/allow_url_fopen = Off/allow_url_fopen = On/g' /etc/php5/fpm/php.ini
RUN perl -pi -e 's/expose_php = On/expose_php = Off/g' /etc/php5/fpm/php.ini

# Copy default site conf
COPY default.conf /etc/nginx/sites-available/default

# Copy the init.sh
COPY init.sh /var/www/init.sh
RUN  chmod +x /var/www/init.sh

# Boot up Nginx, and PHP5-FPM when container is started
CMD /var/www/init.sh && service php5-fpm start && nginx

# Set the current working directory
WORKDIR /var/www/html

# Expose port 80
EXPOSE 80
