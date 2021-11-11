FROM nginx:latest

# Copied from jwilder/nginx
#
# Install wget and install/updates certificates
RUN apt-get update \
 && apt-get install -y -q --no-install-recommends \
    ca-certificates \
    wget \
 && apt-get clean \
 && rm -r /var/lib/apt/lists/*

# Configure Nginx and apply fix for very long server names
RUN echo "daemon off;" >> /etc/nginx/nginx.conf \
 && sed -i 's/^http {/&\n    server_names_hash_bucket_size 128;/g' /etc/nginx/nginx.conf

# Install Forego
RUN wget -P /usr/local/bin https://godist.herokuapp.com/projects/ddollar/forego/releases/current/linux-amd64/forego \
 && chmod u+x /usr/local/bin/forego

RUN wget https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-amd64
RUN mv confd-0.10.0-linux-amd64 /usr/bin/confd
RUN chmod a+x /usr/bin/confd

RUN mkdir -p /etc/confd/conf.d
RUN mkdir -p /etc/confd/templates

COPY confd /etc/confd
COPY app /app/
WORKDIR /app/

VOLUME ["/etc/nginx/certs"]

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["forego", "start", "-r"]
