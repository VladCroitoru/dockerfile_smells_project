FROM nginx:latest

ARG hostip

COPY src/ /var/www  
COPY conf/nginx.conf /etc/nginx/nginx.conf 
COPY conf/mime.types /etc/nginx/mime.types 

#RUN sed -i s/docker-provided-apiServerBaseAddress/$hostip/g /var/www/config.js