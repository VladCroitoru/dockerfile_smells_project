FROM nginx

RUN apt-get update -qq && apt-get install -y geoip-database wget

RUN wget -N http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
RUN gunzip GeoIP.dat.gz
RUN wget -N http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
RUN gunzip GeoLiteCity.dat.gz

RUN mkdir /etc/nginx/geoip/
RUN mv GeoIP.dat /etc/nginx/geoip/
RUN mv GeoLiteCity.dat /etc/nginx/geoip/

COPY ./static /usr/share/nginx/html
ENV ESC='$'
COPY nginx.tmpl /etc/nginx/nginx.tmpl
CMD /bin/sh -c "envsubst < /etc/nginx/nginx.tmpl > /etc/nginx/nginx.conf && nginx -g 'daemon off;' || cat /etc/nginx/nginx.conf"
