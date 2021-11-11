FROM coding4m/proxywall
MAINTAINER coding4m@gmail.com

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list

ENV NGINX_VERSION 1.10.1-1~jessie
ENV NGINX_ENABLED_SITES /etc/nginx/enabled-sites
ENV NGINX_ENABLED_CERTS /etc/nginx/enabled-certs
ENV NGINX_ENABLED_PASSWDS /etc/nginx/enabled-passwds

ENV PROXYWALL_HTTP_PORT 80
ENV PROXYWALL_HTTPS_PORT 443
ENV PROXYWALL_TEMPLATE_SRC /etc/nginx/nginx.tmpl
ENV PROXYWALL_TEMPLATE_DEST /etc/nginx/conf.d/default.conf
ENV PROXYWALL_POST_CMD "nginx -s reload"

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget tar vim libssl1.0.0 ca-certificates nginx=$NGINX_VERSION && \
    rm -rf /var/lib/apt/lists/*

RUN wget -P /tmp https://bin.equinox.io/c/ekMN3bCZFUn/forego-stable-linux-amd64.tgz
#RUN wget -P /usr/bin https://godist.herokuapp.com/projects/ddollar/forego/releases/current/linux-amd64/forego
RUN tar zxf /tmp/forego-stable-linux-amd64.tgz -C /usr/bin && rm -f /tmp/forego-stable-linux-amd64.tgz
RUN chmod u+x /usr/bin/forego

RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

RUN openssl dhparam -out /etc/nginx/nginx.pem 2048
ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./nginx.errors.conf /etc/nginx/nginx.errors.conf
ADD ./nginx.tmpl /etc/nginx/nginx.tmpl

ADD ./html /app/html
ADD ./Procfile /app/
ADD ./app.sh /app/
RUN chmod +x /app/app.sh
WORKDIR /app/

EXPOSE 80 443
VOLUME ["$NGINX_ENABLED_SITES", "$NGINX_ENABLED_CERTS", "$NGINX_ENABLED_PASSWDS"]
CMD ["/bin/bash", "/app/app.sh"]