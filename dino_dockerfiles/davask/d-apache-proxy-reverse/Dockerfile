FROM davask/d-apache:2.4-u16.04
MAINTAINER davask <docker@davaskweblimited.com>
USER root
LABEL dwl.server.proxy="proxy"

# http://stackoverflow.com/questions/7312215/is-there-a-way-to-remove-apaches-reverse-proxy-request-headers?answertab=votes#tab-top
# https://www.x4b.net/kb/RealIP-Apache

# install proxy
RUN a2enmod \
proxy \
proxy_http \
proxy_ajp \
deflate \
proxy_balancer \
proxy_connect \
proxy_html \
xml2enc

COPY ./build/dwl/etc/apache2/sites-available/* /dwl/etc/apache2/sites-available/
RUN cp -rdf /dwl/etc/apache2/sites-available/0000_proxy.rules_0.conf /etc/apache2/sites-available/0000_proxy.rules_0.conf

RUN chmod +x /dwl/init.sh && chown root:sudo -R /dwl
USER admin
