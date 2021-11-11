FROM registry.access.redhat.com/ubi8/ubi-minimal:latest AS manifest

COPY .git /tmp/.git

RUN cd /tmp && \
    sha=$(cat .git/HEAD | cut -d " " -f 2) && \
    if [[ "$(cat .git/HEAD)" == "ref:"* ]]; then sha=$(cat .git/$sha); fi && \
    echo "$(date +"%Y%m%d%H%M%S")-$sha" > /tmp/BUILD

FROM registry.access.redhat.com/ubi8/ubi:8.4

ARG ARCH=x86_64

LABEL name="Httpd" \
      summary="Httpd Image" \
      vendor="ManageIQ" \
      description="Apache HTTP Server"

RUN dnf -y --disableplugin=subscription-manager --setopt=tsflags=nodocs install \
      http://mirror.centos.org/centos/8-stream/BaseOS/${ARCH}/os/Packages/centos-stream-repos-8-2.el8.noarch.rpm \
      http://mirror.centos.org/centos/8-stream/BaseOS/${ARCH}/os/Packages/centos-gpg-keys-8-2.el8.noarch.rpm && \
    dnf -y --disableplugin=subscription-manager module enable mod_auth_openidc && \
    dnf -y --disableplugin=subscription-manager --setopt=tsflags=nodocs install \
      httpd \
      mod_auth_openidc \
      mod_ssl \
      procps-ng && \
    dnf clean all && \
    rm -rf /var/cache/dnf && \
    chmod -R g+w /etc/pki/ca-trust && \
    chmod -R g+w /usr/share/pki/ca-trust-legacy

# Fix permissions so that httpd can run in the restricted scc
RUN chgrp root /var/run/httpd && chmod g+rwx /var/run/httpd  && \
    chgrp root /var/log/httpd && chmod g+rwx /var/log/httpd

# Remove any existing configs in conf.d and don't try to bind to port 80
RUN rm -f /etc/httpd/conf.d/* && \
    sed -i '/^Listen 80/d' /etc/httpd/conf/httpd.conf && \
    sed -i 's+ErrorLog "logs/error_log"+ErrorLog "/dev/stderr"+g' /etc/httpd/conf/httpd.conf && \
    sed -i 's+CustomLog "logs/access_log" combined+CustomLog "/dev/stdout" combined+g' /etc/httpd/conf/httpd.conf

COPY container-assets/cmd /cmd

RUN mkdir -p /opt/manageiq/manifest
COPY --from=manifest /tmp/BUILD /opt/manageiq/manifest

EXPOSE 8080

CMD ["/cmd"]
