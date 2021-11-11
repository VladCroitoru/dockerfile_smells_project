FROM openresty/openresty:1.15.8.3-xenial

RUN mkdir -p /etc/resty-auto-ssl /etc/resty-auto-ssl/storage/file \
    && chown -R nobody /etc/resty-auto-ssl \
    && luarocks install lua-resty-auto-ssl
	
RUN mkdir -p /etc/nginx/conf.d \
    && chown www-data -R /etc/nginx
    
RUN mkdir -p /etc/nginx/locations \
    && chown www-data -R /etc/nginx/locations
    
RUN mkdir -p /var/log/nginx/ \
    && chown www-data /var/log/nginx
    
RUN openssl req -new -newkey rsa:2048 -days 3650 -nodes -x509 \
    -subj '/CN=sni-support-required-for-valid-ssl' \
    -keyout /etc/ssl/resty-auto-ssl-fallback.key \
    -out /etc/ssl/resty-auto-ssl-fallback.crt
    
ADD nginx.conf /usr/local/openresty/nginx/conf/nginx.conf
ADD fastcgi_params /etc/nginx/fastcgi_params

ENTRYPOINT ["/usr/local/openresty/bin/openresty", "-g", "daemon off;"]
