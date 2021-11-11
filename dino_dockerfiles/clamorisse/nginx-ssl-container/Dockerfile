FROM nginx
MAINTAINER Berenice Cotero <berenice@cotero.org>


RUN apt-get update
RUN rm -rf /etc/nginx/conf.d/*

ADD ./nginx.conf /etc/nginx/
ADD ./ssl.conf /etc/nginx/conf.d/
ADD ./http.conf /etc/nginx/conf.d/

RUN sed -i 's/access_log.*/access_log \/dev\/stdout;/g' /etc/nginx/nginx.conf; \
    sed -i 's/error_log.*/error_log \/dev\/stdout info;/g' /etc/nginx/nginx.conf; \
    sed -i 's/^pid/daemon off;\npid/g' /etc/nginx/nginx.conf

ADD ./gen_cert.sh /opt
ADD ./openssl.cnf /opt

RUN chmod 775 opt/gen_cert.sh

ENTRYPOINT ["/opt/gen_cert.sh", "demo-app", "demo-company", "/opt"]
CMD ["nginx"]
