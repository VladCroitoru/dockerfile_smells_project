FROM nginx
COPY . /usr/share/nginx/html
COPY docker/nginx-default.conf.template /etc/nginx/conf.d/default.conf.template

COPY docker-entrypoint.sh /
RUN chmod 755 /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]