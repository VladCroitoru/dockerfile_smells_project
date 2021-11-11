FROM ubuntu:18.04

# install main packages
RUN apt-get update -qq && \
    apt-get install -qy apache2 inotify-tools

# add some files
ADD services/ /etc/service/
RUN chmod -v +x /etc/service/*/run /etc/service/*/finish

# Update apache configuration with this one
RUN a2enmod proxy proxy_http proxy_ajp rewrite deflate substitute headers proxy_balancer proxy_connect proxy_html proxy_wstunnel xml2enc authnz_ldap

# ports and volumes
EXPOSE 80 443
VOLUME /config

COPY apache.conf /etc/apache/apache2.conf

CMD /etc/service/inotify/run
# CMD /usr/sbin/apache2 -f /etc/apache/apache2.conf -DFOREGROUND
