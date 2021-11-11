FROM nginx
ENV NGINX_PORT=80 NGINX_ROOT=/var/www/html/public PHPFPM_HOST=localhost PHPFPM_PORT=3000

COPY entrypoint.sh /entrypoint.sh
COPY default.conf /default.tpl

ENTRYPOINT ["/entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]
