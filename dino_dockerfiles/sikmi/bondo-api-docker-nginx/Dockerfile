FROM nginx:1
COPY config/nginx.conf /etc/nginx/nginx.conf
RUN rm -v /etc/nginx/conf.d/default.conf
COPY config/conf.d/bondo-api.conf /etc/nginx/conf.d/bondo-api.conf
RUN apt-get update && apt-get install -y apache2-utils --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

CMD nginx -g "daemon off;"
