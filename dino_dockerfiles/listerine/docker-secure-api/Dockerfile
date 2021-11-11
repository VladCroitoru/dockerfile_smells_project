FROM ubuntu:latest
MAINTAINER Jonathan Ferretti

RUN apt-get update && apt-get install -y git nginx openssl
RUN git clone https://github.com/LISTERINE/docker-secure-api.git
RUN mv docker-secure-api/nginx.conf /etc/nginx/sites-enabled/default
RUN chown -R www-data /etc/nginx
EXPOSE 4242
CMD /usr/sbin/nginx -g "daemon off;"
