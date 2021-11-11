FROM ubuntu:14.04

RUN apt-get update -qy && apt-get upgrade -qy
RUN apt-get update -q

# Install ngxinx
RUN apt-get install -qy nginx

# Configure Nginx
ADD config/nginx.conf.ubuntu /etc/nginx/nginx.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default

ADD config/jakeschmitz.conf /etc/nginx/sites-enabled/jakeschmitz.conf
ADD config/mime.types /etc/nginx/mime.types

# Move jschmitz files to nginx
ADD ./dist /var/www/html/jakeschmitz

# Expose port 80 for access
EXPOSE 80

# Shell scirpt to start nginx
ADD config/start_server.sh /usr/bin/start_server
RUN chmod +x /usr/bin/start_server

ENTRYPOINT /usr/bin/start_server
