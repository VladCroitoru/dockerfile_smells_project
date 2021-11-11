FROM dockerfile/nodejs
MAINTAINER F4 <dev@f4-group.com>

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget nginx-full
RUN npm install -g grunt
RUN wget -nv --no-check-certificate http://download.elasticsearch.org/kibana/kibana/kibana-3.1.0.tar.gz && \
    tar -xvzf kibana-3.1.0.tar.gz && \
    mkdir -p /usr/share/nginx/www && \
    mv kibana-3.1.0/* /usr/share/nginx/www/ && \
    rm -fr kibana-3.1.0 kibana-3-1.0.tar.gz
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

ADD default /etc/nginx/sites-available/default
ADD config.js /usr/share/nginx/www/config.js
ADD run.sh /usr/local/bin/run
RUN chmod +x /usr/local/bin/run

RUN rm -rf /tmp/*

EXPOSE 80

CMD ["/usr/local/bin/run"]
