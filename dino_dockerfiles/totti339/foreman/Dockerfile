FROM ubuntu:16.04

LABEL maintainer "coveo"

# Config for Foreman
ENV FOREMAN_RELEASE 1.15
ENV FOREMAN_VERSION 1.15.0-1
ENV ADMIN_PASS pass_it

# Install Supervisor
RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y supervisor

# Install Foreman-Installer
RUN apt-get -y install wget && \
    wget -q https://deb.theforeman.org/pubkey.gpg -O- | apt-key add - && \
    echo "deb http://deb.theforeman.org/ xenial $FOREMAN_RELEASE" > /etc/apt/sources.list.d/foreman.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
      foreman foreman-cli foreman-mysql2 foreman-sqlite3 foreman-postgresql

EXPOSE 443

COPY files/supervisord /etc/supervisor

ENTRYPOINT ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
