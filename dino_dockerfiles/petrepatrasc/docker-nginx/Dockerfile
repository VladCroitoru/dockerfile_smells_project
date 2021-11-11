FROM petrepatrasc/docker-ubuntu
MAINTAINER Petre Pătrașc <petre@dreamlabs.ro>
ENV REFRESHED_AT 2016-01-30 21:41:00

# Install nginx
RUN add-apt-repository ppa:nginx/stable && \
    apt-get update -qq && \
    apt-get install -qq -y \
        nginx \
        netcat

# Supervisor
ADD supervisor /etc/supervisor/

# Nginx configurations
RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf && \
    sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf && \
    echo "daemon off;" >> /etc/nginx/nginx.conf;

ADD commands /root/commands
WORKDIR /etc/nginx
EXPOSE 80 443
CMD ["/root/commands/init.sh"]
