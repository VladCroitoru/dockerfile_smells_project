FROM nginx:alpine

COPY . /usr/share/nginx/html
COPY custom /usr/share/nginx/html/custom

# Copy nginx vhost directives
COPY nginx/conf.d /etc/nginx/conf.d
