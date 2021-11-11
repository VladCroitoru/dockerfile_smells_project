FROM nginx

RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \
    && echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends
RUN apt-get update 
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openssl 
RUN openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048 
RUN openssl req -nodes -new -newkey rsa:4096 -out server.csr -sha256 -subj "/C=CL/ST=Nogsantos/L=Nogsantos/O=MyApp/OU=IT Department/CN=localhost" 
RUN mv privkey.pem /etc/ssl/private/server.key 
RUN openssl x509 -req -days 365 -sha256 -in server.csr -signkey /etc/ssl/private/server.key -out /etc/ssl/certs/server.crt
COPY default.conf /etc/nginx/conf.d/default.conf
RUN rm -rf /var/lib/apt/lists/* 