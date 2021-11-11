FROM nginx

RUN mkdir -p /opt/nginx/cache
RUN chown -R www-data:www-data /opt/nginx/

RUN rm /etc/nginx/conf.d/*.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY shadowsocks-org.conf /etc/nginx/conf.d/shadowsocks-org.conf
COPY clients.html /usr/share/nginx/html/clients.html
RUN touch /usr/share/nginx/html/analytics.js

# Install varnish
RUN apt-get update -qq && \
  apt-get upgrade -yqq && \
  apt-get -yqq install varnish && \
  apt-get -yqq clean

COPY default.vcl /etc/varnish/default.vcl
COPY varnish /etc/default/varnish
COPY varnish_service /etc/init.d/varnish

COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD /start.sh

EXPOSE 80
