FROM registry:2
# Requires env CONFIG_BUCKET for s3 bucket to use for config.

RUN apt-get update
RUN apt-get -y install nginx awscli

# Setup for proxy
RUN service nginx stop
ADD resources/docker-registry.site /etc/nginx/sites-available/docker-registry
ADD resources/entrypoint.sh /usr/bin/entrypoint.sh

RUN ln -s /etc/nginx/sites-available/docker-registry /etc/nginx/sites-enabled/docker-registry

ENTRYPOINT entrypoint.sh
