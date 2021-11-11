FROM nginx:1.13

# Copy configuration
COPY nginx.conf mime.types /etc/nginx/
COPY default.conf health-check.conf /etc/nginx/conf.d/

WORKDIR /var/www/public
EXPOSE 80 81 443
