FROM ubuntu:latest
MAINTAINER George Jiglau <george@mux.ro>


# Install add-apt-repository
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qy && \
    apt-get install --no-install-recommends -qy software-properties-common


# Install Nginx
RUN add-apt-repository -y ppa:nginx/stable && \
    apt-get update -q && \
    apt-get install --no-install-recommends -qy nginx && \
    chown -R www-data:www-data /var/lib/nginx && \
    rm -f /etc/nginx/sites-available/default


# Install confd
ADD https://github.com/kelseyhightower/confd/releases/download/v0.9.0/confd-0.9.0-linux-amd64 /usr/local/bin/confd
RUN chmod u+x /usr/local/bin/confd && \
    mkdir -p /etc/confd/conf.d && \
    mkdir -p /etc/confd/templates

# Add confd configuration files
ADD ./src/conf.d/kubernetes-nginx.toml /etc/confd/conf.d/kubernetes-nginx.toml
ADD ./src/templates/kubernetes.conf.tmpl /etc/confd/templates/kubernetes.conf.tmpl

# Add confd watcher
ADD ./src/confd-watch /opt/confd-watch
RUN chmod +x /opt/confd-watch

# Expose http and https ports
EXPOSE 80 443

# Run the confd watcher by default
CMD /opt/confd-watch
