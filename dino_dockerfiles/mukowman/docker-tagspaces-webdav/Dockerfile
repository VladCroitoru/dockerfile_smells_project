FROM ubuntu:trusty
ENV TAGSPACES_VERSION 2.7.5
RUN apt-get update && apt-get install -y nginx nginx-extras apache2-utils && apt-get install -y wget unzip

VOLUME /var/dav
EXPOSE 80
COPY webdav.conf /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/sites-enabled/*

COPY entrypoint.sh /
RUN chmod +x entrypoint.sh \
 && wget https://github.com/tagspaces/tagspaces/releases/download/v${TAGSPACES_VERSION}/tagspaces-${TAGSPACES_VERSION}-web.zip \
 && unzip tagspaces-${TAGSPACES_VERSION}-web.zip \
 && mv tagspaces /usr/share/nginx/www \
 && rm -rf tagspaces-${TAGSPACES_VERSION}-web.zip
CMD nginx -g "daemon off;"
