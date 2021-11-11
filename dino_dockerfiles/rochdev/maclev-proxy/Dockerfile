FROM nginx:1
COPY nginx.conf /etc/nginx/nginx.conf
COPY sites-available /etc/nginx/sites-available
RUN mkdir -p /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/* /etc/nginx/sites-enabled/
