FROM nginx:stable

MAINTAINER Milo Casagrande <milo.casagrande@linaro.org>
LABEL Version="1.0" Description="Customized nginx Docker image for git://ci"

COPY nginx.conf /etc/nginx/nginx.conf
COPY nginx-custom.conf /etc/nginx/conf.d/
COPY artifact-servers.conf /etc/nginx/conf.d/

# Copy the websites.
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir -p /etc/nginx/sites-enabled/
COPY websites/artifacts.conf /etc/nginx/sites-enabled/00-artifacts.conf
COPY websites/hawkbit.conf /etc/nginx/sites-enabled/01-hawkbit.conf
COPY websites/lava.conf /etc/nginx/sites-enabled/01-lava.conf
