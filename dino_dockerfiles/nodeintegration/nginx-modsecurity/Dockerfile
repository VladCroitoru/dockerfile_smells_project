FROM nginx:stable

MAINTAINER Brendan Beveridge <brendan@nodeintegration.com.au>

ENV MODSECURITY_VERSION 2.9.0

RUN cd /opt && \
    echo "deb-src http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -qy git wget dpkg-dev apache2-dev libpcre3-dev libxml2-dev && \
    apt-get source nginx && \
    apt-get -qy build-dep nginx && \
\
    wget -O /opt/modsecurity-${MODSECURITY_VERSION}.tar.gz https://www.modsecurity.org/tarball/2.9.0/modsecurity-${MODSECURITY_VERSION}.tar.gz && \
    cd /opt && tar -zxvf modsecurity-${MODSECURITY_VERSION}.tar.gz && \
\
    cd /opt/modsecurity-${MODSECURITY_VERSION} && \
    ./configure --enable-standalone-module --disable-mlogc && \
    make && \
\
    cd /opt/nginx-* && \
    sed -i -e 's%\./configure%./configure --add-module=/opt/modsecurity-${MODSECURITY_VERSION}/nginx/modsecurity --with-http_stub_status_module%' debian/rules && \
    dpkg-buildpackage -b && \
    dpkg -i /opt/nginx_*.deb && \
\
    cp /opt/modsecurity-${MODSECURITY_VERSION}/modsecurity.conf-recommended /etc/nginx/modsecurity.conf && \
    cp /opt/modsecurity-${MODSECURITY_VERSION}/unicode.mapping /etc/nginx/ && \
\
    cd /usr/src && \
    git clone https://github.com/SpiderLabs/owasp-modsecurity-crs.git && \
\
    apt-get remove -qy --purge git wget dpkg-dev apache2-dev libpcre3-dev libxml2-dev && \
    apt-get -qy autoremove && \
    rm -rf /opt/modsecurity-* && \
    rm -rf /opt/nginx* && \
    rm -rf /var/lib/apt/lists/*

RUN ln -sf /dev/stdout /var/log/modsec_audit.log
RUN mkdir /etc/nginx/modsecurity-data && \
    chown nginx: /etc/nginx/modsecurity-data && \
    cat /usr/src/owasp-modsecurity-crs/crs-setup.conf.example /usr/src/owasp-modsecurity-crs/rules/*.conf > /etc/nginx/modsecurity.conf && \
    cp /usr/src/owasp-modsecurity-crs/rules/*.data /etc/nginx/ && \
    sed -i -e 's%location / {%location / {\n        ModSecurityEnabled on;\n        ModSecurityConfig modsecurity.conf;%' /etc/nginx/conf.d/default.conf && \
    echo "SecAuditLog /var/log/modsec_audit.log" >> /etc/nginx/modsecurity.conf && \
    echo "SecRuleEngine On" >> /etc/nginx/modsecurity.conf && \
    #echo 'SecDefaultAction "phase:1,deny,log"' >> /etc/nginx/modsecurity.conf
    echo "SecDataDir /etc/nginx/modsecurity-data" >> /etc/nginx/modsecurity.conf

#ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]

