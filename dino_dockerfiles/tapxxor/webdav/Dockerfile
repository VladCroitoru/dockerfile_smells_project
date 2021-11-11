FROM alpine:3.7

MAINTAINER tapxxor theofanis.pispirigkos@gmail.com

ENV SERVER_NAME webdav.kube-system.svc.cluster.local 
ENV DAV_CONF /etc/apache2/conf.d/dav.conf
ENV HTTPD_CONF /etc/apache2/httpd.conf
ENV PASSWD /usr/user.passwd
ENV REALM webdav

ADD entrypoint.sh .

# ensure www-data user exists
RUN set -x \
	&& addgroup -g 82 -S www-data \
    && adduser -u 82 -D -S -G www-data www-data

# add webdav and apache
RUN apk add --no-cache apache2-webdav=2.4.29-r1 apache2-utils=2.4.29-r1

# create the upload folder
RUN mkdir -p /uploads     \
    && chmod 770 /uploads \
    && chown -R www-data:www-data /uploads             
   
# The User/Group specified in httpd.conf needs to have write permissions
# on the directory where the DavLockDB is placed and on any directory where
# "Dav On" is specified.
RUN mkdir -p /run/apache2     \
    && mkdir -p /var/lib/dav  \
    && chown www-data:www-data /var/lib/dav  \
    && chmod 770 /var/lib/dav                \
    && chmod 755 /entrypoint.sh

EXPOSE 80 

CMD ["/entrypoint.sh"]
