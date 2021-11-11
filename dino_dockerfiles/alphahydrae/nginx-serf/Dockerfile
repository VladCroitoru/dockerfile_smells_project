FROM alphahydrae/nginx-serf-docker-base:2.0.0

# Install nginx-serf dependencies
RUN mkdir -p /opt/nginx-serf
ADD package.json /opt/nginx-serf/package.json
RUN cd /opt/nginx-serf && npm install --production

# Install nginx-serf
RUN mkdir -p /etc/nginx-serf /etc/ssl/private /var/www
ADD bin /opt/nginx-serf/bin
ADD lib /opt/nginx-serf/lib
ADD templates /opt/nginx-serf/templates
ADD docker/handle-serf-event.sh /opt/nginx-serf/

# Add default serf configuration file
RUN echo "{}" > /etc/serf.conf

# Add s6 serf service
RUN mkdir -p /etc/services.d/serf
ADD docker/run-serf.sh /etc/services.d/serf/run

# Add s6 nginx service
RUN mkdir -p /etc/services.d/nginx
ADD docker/run-nginx.sh /etc/services.d/nginx/run
ADD docker/finish-all.sh /etc/services.d/nginx/finish

# Add s6 nginx-serf service
RUN mkdir -p /etc/services.d/nginx-serf
ADD docker/run-nginx-serf.sh /etc/services.d/nginx-serf/run
ADD docker/finish-all.sh /etc/services.d/nginx-serf/finish

# Add s6 serf graceful shutdown script
ADD docker/serf-graceful-shutdown.sh /etc/cont-finish.d/

# Set up nginx directories
RUN mkdir /etc/nginx/sites-serf \
    && rm -fr /etc/nginx/nginx.conf /etc/nginx/sites-available/* /etc/nginx/sites-enabled/*

# Allow the serf graceful shutdown script to last up to 10 seconds
ENV S6_KILL_FINISH_MAXTIME 10000

# Expose http/s ports
EXPOSE 80
EXPOSE 443

# Expose serf port
EXPOSE 7946
