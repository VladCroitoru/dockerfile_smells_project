FROM nginx:1.13.3

ENV NGINX_BASE /docker-nuget
ENV UPLOAD_MAX_FILESIZE 20M

# Activate the nginx configuration
RUN rm /etc/nginx/conf.d/default*.conf
COPY ./nuget.conf /etc/nginx/conf.d/

# Add the scripts which modify nginx config
COPY ./patch-filesize.sh ./patch-routes.sh $NGINX_BASE/

# Modify nginx config
RUN chmod +x $NGINX_BASE/patch-filesize.sh && \
    chmod +x $NGINX_BASE/patch-routes.sh && \
    sleep 1 && \
    $NGINX_BASE/patch-filesize.sh && \
    $NGINX_BASE/patch-routes.sh