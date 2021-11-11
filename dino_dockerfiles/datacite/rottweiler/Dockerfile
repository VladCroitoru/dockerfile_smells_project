FROM phusion/baseimage:0.10.1
LABEL maintainer="mfenner@datacite.org"

# Set correct environment variables.
ENV HOME /home/app
ENV OAUTH_PROVIDER_VERSION 0.2.1

# Use baseimage-docker's init process.
CMD ["/sbin/my_init"]

# Update installed APT packages
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \
    apt-get install ntp wget tzdata -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# install netlify-cms-oauth-provider
RUN wget https://github.com/igk1972/netlify-cms-oauth-provider-go/releases/download/$OAUTH_PROVIDER_VERSION/netlify-cms-oauth-provider_linux-amd64 && \
    cp netlify-cms-oauth-provider_linux-amd64 /usr/local/bin/netlify-cms-oauth-provider && \
    chmod +x /usr/local/bin/netlify-cms-oauth-provider

# Use Amazon NTP servers
COPY vendor/docker/ntp.conf /etc/ntp.conf

# Add Runit script for service
RUN mkdir /etc/service/netlify-cms-oauth-provider
ADD vendor/docker/netlify-cms-oauth-provider.sh /etc/service/netlify-cms-oauth-provider/run

# Expose web
EXPOSE 80
