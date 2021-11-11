FROM registry.access.redhat.com/ubi8/ubi-init:8.3
MAINTAINER ManageIQ https://github.com/ManageIQ/container-httpd

ARG ARCH=x86_64
ARG DBUS_API_REF=master

LABEL name="auth-httpd" \
      vendor="ManageIQ" \
      url="http://manageiq.org/" \
      summary="httpd image with external authentication" \
      description="An httpd image which includes packages and configuration necessary for handling external authentication."

RUN dnf -y --disableplugin=subscription-manager install \
      http://mirror.centos.org/centos/8.3.2011/BaseOS/${ARCH}/os/Packages/centos-linux-repos-8-2.el8.noarch.rpm \
      http://mirror.centos.org/centos/8.3.2011/BaseOS/${ARCH}/os/Packages/centos-gpg-keys-8-2.el8.noarch.rpm && \
    dnf -y --disableplugin=subscription-manager module enable mod_auth_openidc && \
    dnf -y --disableplugin=subscription-manager install --setopt=tsflags=nodocs \
    httpd \
    mod_ssl \
    # SSSD Packages \
    sssd \
    sssd-dbus \
    # Apache External Authentication Module Packages \
    mod_auth_gssapi \
    mod_authnz_pam \
    mod_intercept_form_submit \
    mod_lookup_identity \
    mod_auth_mellon \
    mod_auth_openidc \
    # IPA External Authentication Packages \
    c-ares \
    certmonger \
    ipa-client \
    ipa-admintools \
    # Active Directory External Authentication Packages \
    adcli \
    realmd \
    oddjob \
    oddjob-mkhomedir \
    samba-common \
    samba-common-tools && \
    dnf --disableplugin=subscription-manager clean all

## Remove any existing configurations
RUN rm -f /etc/httpd/conf.d/*

RUN dnf -y --disableplugin=subscription-manager module enable ruby:2.6 && \
    dnf -y --disableplugin=subscription-manager --setopt=tsflags=nodocs install ruby

## Install DBus API Service
ENV HTTPD_DBUS_API_SERVICE_DIRECTORY=/opt/dbus_api_service
ENV HTTPD_DBUS_API_SERVICE_PORT=8081
RUN mkdir -p ${HTTPD_DBUS_API_SERVICE_DIRECTORY}
RUN cd ${HTTPD_DBUS_API_SERVICE_DIRECTORY} && \
    curl -L https://github.com/ManageIQ/dbus_api_service/tarball/${DBUS_API_REF} | tar vxz -C ${HTTPD_DBUS_API_SERVICE_DIRECTORY} --strip 1 && \
    gem install bundler && \
    bundle config set without test && \
    bundle install
COPY container-assets/dbus-api.service /usr/lib/systemd/system/dbus-api.service

## Create the mount point for the authentication configuration files
RUN mkdir /etc/httpd/auth-conf.d

COPY container-assets/save-container-environment /usr/bin
COPY container-assets/initialize-httpd-auth.sh   /usr/bin

COPY container-assets/initialize-httpd-auth.service /usr/lib/systemd/system/initialize-httpd-auth.service

## Make sure sssd has the right startup conditions
RUN  mkdir -p /etc/systemd/system/sssd.service.d
COPY container-assets/sssd-startup.conf /etc/systemd/system/sssd.service.d/startup.conf

## Make sure httpd has the environment variables needed for external auth
RUN  mkdir -p /etc/systemd/system/httpd.service.d
COPY container-assets/httpd-environment.conf /etc/systemd/system/httpd.service.d/environment.conf

## Copy the pages that must be served by this httpd and cannot be proxied.
RUN mkdir -p /var/www/html/proxy_pages
COPY container-assets/invalid_sso_credentials.js /var/www/html/proxy_pages/

EXPOSE 8080
EXPOSE 8081

WORKDIR /etc/httpd

RUN systemctl enable initialize-httpd-auth sssd httpd dbus-api

CMD [ "/sbin/init" ]
