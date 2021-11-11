FROM nginx:1.17.9-alpine

# use nginx server to serve files
COPY dist/* /usr/share/nginx/html/

# update configuration for HTML5 push state
COPY infra/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80