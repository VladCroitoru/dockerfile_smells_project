FROM nginx:1.13

# Install extra nginx plugins
# RUN apt-get install nginx-extras

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf
COPY empty.gif /etc/nginx/html/empty.gif

EXPOSE 80
