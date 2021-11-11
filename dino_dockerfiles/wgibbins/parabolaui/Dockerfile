# Ubuntu base nginx
FROM ubuntu:14.04
MAINTAINER PostModernLuddite@gmail.com
RUN \  
  apt-get update && \
  apt-get install -y nginx && \
  rm -rf /var/lib/apt/lists/* 

RUN rm -v      /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY *.html    /usr/share/nginx/html/ 
RUN mkdir      /usr/share/nginx/html/js 
COPY *.js      /usr/share/nginx/html/js/

EXPOSE 8080

CMD ["nginx"]

