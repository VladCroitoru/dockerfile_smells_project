FROM nginx:alpine

# Setup catchall as ayodooit.com.html
COPY . /usr/share/nginx/html

# Copy nginx vhost directives
COPY nginx/conf.d /etc/nginx/conf.d
