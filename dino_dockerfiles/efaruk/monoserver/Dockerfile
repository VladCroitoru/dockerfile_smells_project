# Base Image
FROM mono

# LABEL
LABEL author="efaruk"
LABEL version="1.0.0"
LABEL description="Mono Server image based mono"
MAINTAINER E. Faruk Pehlivanli

# Copy
ADD ./init.sh /usr/local/bin/init.sh

# Prepare
RUN chmod a+x /usr/local/bin/init.sh \
    && apt-get update \
    && apt-get install nginx supervisor -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/* 


ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD ./nginx.conf /etc/nginx/sites-available/default

RUN ln -s -f /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

# Define
# Nginx Listens 80 and App should listen 8888. Nginx configured as reverse proxy and static file handler...
EXPOSE 80
ENTRYPOINT ["/usr/local/bin/init.sh"]

