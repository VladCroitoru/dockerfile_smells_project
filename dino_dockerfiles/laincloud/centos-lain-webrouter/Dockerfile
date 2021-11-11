FROM laincloud/centos-lain:20170217

COPY libunwind-1.1-3.sdl7.x86_64.rpm /root/libunwind-1.1-3.sdl7.x86_64.rpm
COPY tengine-2.1.1-3.modsec_2.9.0.el7.centos.x86_64.rpm /root/tengine-2.1.1-3.modsec_2.9.0.el7.centos.x86_64.rpm
COPY tengine-filesystem-2.1.1-3.modsec_2.9.0.el7.centos.noarch.rpm /root/tengine-filesystem-2.1.1-3.modsec_2.9.0.el7.centos.noarch.rpm

RUN yum install -y /root/libunwind-1.1-3.sdl7.x86_64.rpm \
    /root/tengine-filesystem-2.1.1-3.modsec_2.9.0.el7.centos.noarch.rpm \
    /root/tengine-2.1.1-3.modsec_2.9.0.el7.centos.x86_64.rpm \
    logrotate crontabs \
    && yum -y clean all \
    && rm -rf /root/*.rpm \
    && pip install supervisor \
    && mkdir -p /var/log/supervisor \
    && mkdir -p /var/log/watcher \
    && mv /etc/tengine /etc/nginx \
    && ln -s /etc/nginx /etc/tengine \
    && mv /etc/nginx/tengine.conf /etc/nginx/nginx.conf \
    && ln -s /etc/nginx/nginx.conf /etc/tengine/tengine.conf \
    && ln -s /usr/sbin/tengine /usr/sbin/nginx \
    && rm -rf /var/log/tengine \
    && ln -s /var/log/nginx /var/log/tengine

VOLUME ["/var/cache/nginx"]
VOLUME ["/var/log/nginx"]
VOLUME ["/var/log/supervisor"]
VOLUME ["/var/log/watcher"]

EXPOSE 80 443
