FROM registry.access.redhat.com/ubi8/ubi-minimal:latest AS manifest

COPY .git /tmp/.git

RUN cd /tmp && \
    sha=$(cat .git/HEAD | cut -d " " -f 2) && \
    if [[ "$(cat .git/HEAD)" == "ref:"* ]]; then sha=$(cat .git/$sha); fi && \
    echo "$(date +"%Y%m%d%H%M%S")-$sha" > /tmp/BUILD

FROM registry.access.redhat.com/ubi8/ubi-init:8.4
MAINTAINER ManageIQ https://github.com/ManageIQ/container-httpd

ARG ARCH=x86_64
ARG DBUS_API_REF=master

LABEL name="auth-httpd" \
      vendor="ManageIQ" \
      url="http://manageiq.org/" \
      summary="httpd image with external authentication" \
      description="An httpd image which includes packages and configuration necessary for handling external authentication."

RUN dnf -y --disableplugin=subscription-manager --setopt=tsflags=nodocs install \
      http://mirror.centos.org/centos/8-stream/BaseOS/${ARCH}/os/Packages/centos-stream-repos-8-2.el8.noarch.rpm \
      http://mirror.centos.org/centos/8-stream/BaseOS/${ARCH}/os/Packages/centos-gpg-keys-8-2.el8.noarch.rpm && \
    dnf -y --disableplugin=subscription-manager module enable mod_auth_openidc && \
    dnf -y --disableplugin=subscription-manager --setopt=tsflags=nodocs install \
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
    dnf clean all && \
    rm -rf /var/cache/dnf

## Remove any existing configurations
RUN rm -f /etc/httpd/conf.d/* && \
    sed -i 's+ErrorLog "logs/error_log"+ErrorLog "/dev/stderr"+g' /etc/httpd/conf/httpd.conf && \
    sed -i 's+CustomLog "logs/access_log" combined+CustomLog "/dev/stdout" combined+g' /etc/httpd/conf/httpd.conf

RUN dnf -y --disableplugin=subscription-manager module enable ruby:2.6 && \
    dnf -y --disableplugin=subscription-manager --setopt=tsflags=nodocs install \
      ruby && \
    dnf clean all && \
    rm -rf /var/cache/dnf

## Install DBus API Service
ENV HTTPD_DBUS_API_SERVICE_DIRECTORY=/opt/dbus_api_service
ENV HTTPD_DBUS_API_SERVICE_PORT=8081
RUN mkdir -p ${HTTPD_DBUS_API_SERVICE_DIRECTORY}
RUN cd ${HTTPD_DBUS_API_SERVICE_DIRECTORY} && \
    curl -L https://github.com/ManageIQ/dbus_api_service/tarball/${DBUS_API_REF} | tar vxz -C ${HTTPD_DBUS_API_SERVICE_DIRECTORY} --strip 1 && \
    echo "gem: --no-document" > ~/.gemrc && \
    gem install bundler && \
    bundle config set without test && \
    bundle install --jobs=3 --retry=3 && \
    rm -rf /usr/share/gems/cache/* && \
    find /usr/share/gems/gems/ -name *.o -type f -delete && \
    find /usr/share/gems/gems/ -maxdepth 2 -name docs -type d -exec rm -r {} + && \
    find /usr/share/gems/gems/ -maxdepth 2 -name spec -type d -exec rm -r {} + && \
    find /usr/share/gems/gems/ -maxdepth 2 -name test -type d -exec rm -r {} +
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

RUN mkdir -p /opt/manageiq/manifest
COPY --from=manifest /tmp/BUILD /opt/manageiq/manifest

EXPOSE 8080
EXPOSE 8081

WORKDIR /etc/httpd

RUN systemctl enable initialize-httpd-auth sssd httpd dbus-api

CMD [ "/sbin/init" ]
