FROM ubuntu:20.04
LABEL Maintainer="PV"
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y nginx curl tree wget
CMD [ "/usr/sbin/nginx", "-g", "daemon off;" ]
EXPOSE 80
COPY . /var/www/html
