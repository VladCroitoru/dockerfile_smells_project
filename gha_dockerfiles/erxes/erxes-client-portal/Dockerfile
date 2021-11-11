ARG BASE_IMAGE
FROM $BASE_IMAGE
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
COPY build /usr/share/nginx/html/help