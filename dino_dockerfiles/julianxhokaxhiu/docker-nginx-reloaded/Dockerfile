FROM nginx:stable-alpine
MAINTAINER Julian Xhokaxhiu <info at julianxhokaxhiu dot com>

# Environment variables
#######################

ENV NGINX_CERTS /etc/nginx/certs
ENV NGINX_VHOSTD /etc/nginx/vhost.d
ENV NGINX_HTPASSWD /etc/nginx/htpasswd
ENV LE_CONFIG_HOME /etc/acme.le
ENV DEFAULT_ACCOUNT_KEY_LENGTH 4096
ENV DEFAULT_DOMAIN_KEY_LENGTH 4096

# Configurable environment variables
####################################

# Custom DNS where to forward your request, if not found inside the DNS Server.
# By default this will be forwarded to Google DNS for IPv4 and IPv6 requests.
# See https://doc.powerdns.com/md/recursor/settings/#forward-zones
ENV DNSALT1 '8.8.8.8'
ENV DNSALT2 '8.8.4.4'
ENV DNS6ALT1 '2001:4860:4860::8888'
ENV DNS6ALT2 '2001:4860:4860::8844'

# Create Volume entry points
############################

VOLUME $NGINX_CERTS
VOLUME $NGINX_VHOSTD
VOLUME $NGINX_HTPASSWD
VOLUME $LE_CONFIG_HOME

# Copy required files and fix permissions
#########################################

COPY src/ /root/

# Create missing directories
############################

RUN mkdir -p $NGINX_CERTS \
    mkdir -p $NGINX_VHOSTD \
    mkdir -p $NGINX_HTPASSWD \
    mkdir -p $LE_CONFIG_HOME \
    mkdir -p /run/nginx

# Set the work directory
########################

WORKDIR /root

# Fix permissions
#################

RUN chmod -R 0644 * \
    && chmod -R 0755 *.sh

# Install required packages
##############################

RUN apk --update add --no-cache \
    bash \
    curl \
    libressl \
    libidn \
    vim \
    socat \
    # Supervisor Daemon
    supervisor \
    # NodeJS + NPM
    nodejs \
    npm

# Install the acme.sh client
############################

RUN curl https://get.acme.sh | sh

# Install dynsdjs + docker plugin
#################################

RUN npm install --only=prod --no-optional -g dynsdjs \
    && npm install --only=prod --no-optional -g dynsdjs-plugin-docker

# Add the referral-spam.conf to nginx
#####################################

ADD https://raw.githubusercontent.com/Stevie-Ray/referrer-spam-blocker/master/referral-spam.conf /etc/nginx/

# Cleanup
#########

RUN find /usr/local \
      \( -type d -a -name test -o -name tests \) \
      -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
      -exec rm -rf '{}' + \
    && rm -rf /var/cache/apk/*

# Replace default configurations
################################
RUN rm /etc/supervisord.conf \
    && mv /root/supervisord.conf /etc \
    && cp -Rf /root/nginx/* /etc/nginx \
    && rm -Rf /root/nginx

# Allow redirection of stdout to docker logs
############################################
RUN ln -sf /proc/1/fd/1 /var/log/docker.log

# Expose required ports
#######################

EXPOSE 53/udp
EXPOSE 80
EXPOSE 443

# Change Shell
##############
SHELL ["/bin/bash", "-c"]

# Set the entry point to init.sh
###########################################

ENTRYPOINT /root/init.sh
