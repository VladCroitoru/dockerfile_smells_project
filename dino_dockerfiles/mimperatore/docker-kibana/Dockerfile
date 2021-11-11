FROM nginx
MAINTAINER mimperatore@gmail.com

# Replace nginx default site with Kibana, making it accessible on localhost:80.
#RUN unlink /etc/nginx/sites-enabled/default
#ADD config/etc/nginx/kibana.conf /etc/nginx/sites-enabled/default

# Install Kibana.
RUN \
  export DEBIAN_FRONTEND=noninteractive && \
  cd /tmp && \
  apt-get update && \
  apt-get install -y apt-utils ca-certificates wget && \
  wget https://download.elasticsearch.org/kibana/kibana/kibana-3.1.2.tar.gz && \
  tar xvzf kibana-3.1.2.tar.gz && \
  rm -f kibana-3.1.2.tar.gz && \
  mv kibana-3.1.2 /usr/share/kibana && \
  unlink /etc/nginx/conf.d/default.conf && \
  echo "daemon off;" >> /etc/nginx/nginx.conf

#COPY static-html-directory /usr/share/nginx/html
COPY config/etc/nginx/kibana.conf /etc/nginx/conf.d/kibana.conf

# Copy kibana config.
ADD config/etc/kibana/config.js /usr/share/kibana/config.js

# Define working directory.
WORKDIR /

CMD ["/usr/sbin/nginx"]

# Expose nginx http ports
EXPOSE 80
#EXPOSE 443
