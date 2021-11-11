FROM ubuntu:16.04

LABEL maintainer "coveo"

# Config for Foreman
ENV FOREMAN_RELEASE 1.15
ENV FOREMAN_VERSION 1.15.6-1

# Add repo Foreman-plugin
RUN echo "deb http://deb.theforeman.org/ plugins $FOREMAN_RELEASE" > /etc/apt/sources.list.d/foreman-plugins.list 

# Add repo Foreman
RUN  apt-key adv --fetch-keys http://deb.theforeman.org/pubkey.gpg  && \
    echo "deb http://deb.theforeman.org/ xenial $FOREMAN_RELEASE" > /etc/apt/sources.list.d/foreman.list 

# Get laset version
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -y

# Create puppet user and group with defined UID and GID
RUN useradd -u 1000 -U puppet

# Install Supervisor
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
    supervisor \
    cron \
    git \ 
    golang \
    foreman-installer \
    tzdata \
    nfs-common 

# Prerequisite for EFS
RUN mkdir /install && \
    mkdir -p /var/lib/puppet/ssl

# make hostname -f work for foreman-installer
RUN rm -f /usr/share/foreman-installer/checks/hostname.rb && export FACTER_fqdn="$HOSTNAME.docker.local"

RUN foreman-installer \
    --foreman-version=$FOREMAN_VERSION \
    --foreman-db-type=mysql \
    --foreman-db-manage=false \
    --foreman-db-manage-rake=false \
    --foreman-proxy-puppet=false \
    --foreman-proxy-puppetca=false \
    --enable-foreman-plugin-default-hostgroup \
    --no-enable-foreman-proxy \
    --no-enable-puppet \
    --foreman-ssl=false && \
    service foreman stop && \
    service apache2 stop && \
    systemctl disable foreman && \
    systemctl disable apache2

# Clean apt cache
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY files/install /install
RUN chmod +x /install/*.sh

COPY files/supervisord /etc/supervisor
COPY files/foreman/prometheus.rake /usr/share/foreman/lib/tasks/prometheus.rake

EXPOSE 443

ENTRYPOINT ["/install/entrypoint.sh"]
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
