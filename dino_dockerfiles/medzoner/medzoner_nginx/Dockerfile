FROM nginx:1.11

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

RUN rm -rf /var/www
RUN mkdir -p /var/www/html

RUN usermod -u 1000 www-data

## add permissions for nginx user
RUN chown -R www-data:www-data /var/cache/nginx && \
        chown -R www-data:www-data /var/www && \
        chown -R www-data:www-data /var/log/nginx && \
        chown -R www-data:www-data /etc/nginx/conf.d
RUN touch /var/run/nginx.pid && \
        chown -R www-data:www-data /var/run/nginx.pid

USER www-data

CMD ["nginx", "-g", "daemon off;"]
