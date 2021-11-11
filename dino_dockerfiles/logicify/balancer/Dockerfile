FROM logicify/centos7:latest
RUN yum -y update \    
    && yum -y install nginx
    
# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir /etc/nginx/certs && mkdir /etc/nginx/proxy
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./mime.types /etc/nginx/mime.types
COPY ./ssl.conf /etc/nginx/ssl.conf
COPY ./proxy.conf /etc/nginx/proxy.conf

EXPOSE 80 443
VOLUME ["/etc/nginx/proxy", "/etc/nginx/certs"]

CMD ["nginx", "-g", "daemon off;"]
