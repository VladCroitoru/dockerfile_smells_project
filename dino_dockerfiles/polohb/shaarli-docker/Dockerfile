FROM       debian:latest
MAINTAINER polohb <polohb@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Update system and install some packages
RUN apt-get update -y \
&& apt-get install -q -y nginx php5-fpm git \
&& rm -rf /var/lib/apt/lists/*

# Configuration nginx et php
ADD ./scripts/conf.d/ /etc/nginx/conf.d/
ADD ./scripts/sites-available/ /etc/nginx/sites-available/
ADD ./scripts/pool.d/ /etc/php5/fpm/pool.d/


# Install shaarli by cloning git repo
RUN cd /tmp \
    && git clone https://github.com/shaarli/Shaarli.git \
    && rm -rf /var/www \
    && mv /tmp/Shaarli /var/www/ \
    && chown www-data:www-data /var/www -R

VOLUME /var/www/

EXPOSE 8080

ADD ./scripts/startup.sh /opt/startup.sh
RUN chmod +x /opt/startup.sh
CMD ["/opt/startup.sh"]
