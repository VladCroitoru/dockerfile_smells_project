FROM nginx:1
COPY config/nginx.conf /etc/nginx/nginx.conf
RUN rm -v /etc/nginx/conf.d/default.conf
COPY config/conf.d/zexyletter.conf /etc/nginx/conf.d/zexyletter.conf
RUN apt-get update && apt-get install -y apache2-utils --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

CMD htpasswd -cb /etc/nginx/conf.d/.htpasswd $BASIC_AUTH_USER $BASIC_AUTH_PASS && nginx -g "daemon off;"
