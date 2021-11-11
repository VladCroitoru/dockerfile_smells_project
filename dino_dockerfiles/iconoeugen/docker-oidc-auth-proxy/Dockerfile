FROM centos:7
MAINTAINER horatiu@vlad.eu

LABEL name="Apache HTTPD  Reverse-Proxy with OpenID Connect Authentication support"

ENV DOL_BASE_DIR /opt/dol
ENV DOL_TMPL_DIR ${DOL_BASE_DIR}/httpd

ENV MOD_AUTH_OPENIDC_VERSION 2.1.0
ENV MOD_AUTH_OPENIDC_RELEASE_URL https://github.com/pingidentity/mod_auth_openidc/releases/download/v${MOD_AUTH_OPENIDC_VERSION}

RUN yum -y install epel-release \
    && yum -y install httpd nss_wrapper \
    && yum -y install \
        ${MOD_AUTH_OPENIDC_RELEASE_URL}/cjose-0.4.1-1.el7.centos.x86_64.rpm \
        ${MOD_AUTH_OPENIDC_RELEASE_URL}/mod_auth_openidc-${MOD_AUTH_OPENIDC_VERSION}-1.el7.centos.x86_64.rpm \
    && yum clean all

# Relax permissions for nginx directories
RUN for dir in /etc/httpd/conf /etc/httpd/conf.d /etc/httpd/default.d /var/lib/httpd /var/log/httpd /run/httpd ; do \
    mkdir -p ${dir} && chmod -cR g+rwx ${dir} && chgrp -cR root ${dir} ; \
    done

# forward request and error logs to docker log collector
RUN ln -sf /proc/self/fd/1 /var/log/httpd/access_log \
    && ln -sf /proc/self/fd/2 /var/log/httpd/error_log

# Prepare Nginx proxy configuration.
RUN mkdir -p ${DOL_TMPL_DIR}
COPY config/*.in ${DOL_TMPL_DIR}/

# And not the docker entrypoint script.
COPY entrypoint.sh /entrypoint.sh

EXPOSE 8080 8443

ENTRYPOINT ["/entrypoint.sh"]
