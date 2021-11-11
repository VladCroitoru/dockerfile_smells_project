
FROM debian:latest
MAINTAINER polohb <polohb@gmail.com>

RUN apt-get update -y \
    && apt-get install -y build-essential libpcre3 libpcre3-dev libssl-dev curl unzip ffmpeg \
    && rm -rf /var/lib/apt/lists/*

ENV NGINX_V nginx-1.7.5

RUN mkdir -p /opt/nginx/ \
    && cd /opt/nginx \
    && curl --fail --silent --location --retry 3 http://nginx.org/download/${NGINX_V}.tar.gz | gunzip | tar -x   \
    && curl -O --fail --silent --location --retry 3 https://github.com/arut/nginx-rtmp-module/archive/master.zip \
    && unzip  master.zip \
    && rm master.zip \
    && cd ${NGINX_V} \
    && ./configure --with-http_ssl_module --add-module=../nginx-rtmp-module-master \
    && make \
    && make install \
    && cd / \
    && curl --fail --silent --location --retry 3 https://raw.githubusercontent.com/JasonGiedymin/nginx-init-ubuntu/master/nginx -o /etc/init.d/nginx \
    && chmod +x /etc/init.d/nginx \
    && update-rc.d nginx defaults \
    && service nginx start \
    && service nginx stop \
    && cp /opt/nginx/nginx-rtmp-module-master/stat.xsl /usr/local/nginx/html/ \
    && rm -rf /opt/nginx 

ADD ./nginx.conf /usr/local/nginx/conf/nginx.conf

ADD jwplayer /usr/local/nginx/html/


EXPOSE 1935
EXPOSE 80
 
    
CMD /usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf -g "daemon off;"




