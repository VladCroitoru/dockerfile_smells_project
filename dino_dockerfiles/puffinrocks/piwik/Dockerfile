FROM nginx

ENV VERSION=3.0.1

COPY nginx.conf /etc/nginx/nginx.conf
COPY docker-entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]

