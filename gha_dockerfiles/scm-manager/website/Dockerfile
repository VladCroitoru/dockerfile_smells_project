FROM nginx:1.19.2

# if more files are required, ensure .dockerignore does not exclude them
COPY deployment/docker/redirects.conf /etc/nginx/redirects.conf
COPY deployment/docker/nginx.conf /etc/nginx/nginx.conf
COPY public /usr/share/nginx/html

RUN chown -R nginx:nginx /var/cache/nginx

EXPOSE 8000
USER nginx
