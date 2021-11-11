FROM debian:jessie-slim

MAINTAINER jsonoda@getmealticket.com

RUN apt-get update && \
    apt-get install -y nginx php5-fpm php5-cli php5-mysql php5-mcrypt php5-imagick curl php5-curl rsyslog rsyslog-gnutls runit && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Setup runit services
ADD service /etc/service
RUN find /etc/service -type f -name run -exec chmod +x {} \;

# Startup Script Directory
RUN mkdir -p /opt/init/startup

# Setup php5
RUN rm -f /etc/php5/fpm/pool.d/*
ADD www-php5-pool.conf /etc/php5/fpm/pool.d/
ADD php-fpm.conf /etc/php5/fpm/php-fpm.conf

# Create the folder for storing tls certificates for rsyslog
RUN mkdir -p /etc/rsyslog.d/keys/ca.d

# Add the init script
ADD init.sh /opt/init/init.sh
RUN chmod +x /opt/init/init.sh

# Add the docker-friendly rsyslog.conf file
ADD rsyslog.conf /etc/rsyslog.conf

CMD ["/opt/init/init.sh"]
