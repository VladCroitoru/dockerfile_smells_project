FROM nginx:1.11.3
MAINTAINER Jason Wilder mail@jasonwilder.com

ENV DOCKER_GEN_VERSION 0.7.3

# Install wget and install/updates certificates
RUN apt-get update \
 && apt-get install -y -q --no-install-recommends \
    ca-certificates \
    wget \
 && apt-get clean \
 && rm -r /var/lib/apt/lists/* \
# Configure Nginx and apply fix for very long server names
 && echo "daemon off;" >> /etc/nginx/nginx.conf \
 && sed -i 's/.*server_names_hash_bucket_size .*/      server_names_hash_bucket_size 256;\n      client_max_body_size 80M;/g' /etc/nginx/nginx.conf \
# Install Forego
 && wget -P /usr/local/bin https://github.com/jwilder/forego/releases/download/v0.16.1/forego \
 && chmod u+x /usr/local/bin/forego \
 && wget https://github.com/jwilder/docker-gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \
 && tar -C /usr/local/bin -xvzf docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \
 && rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz

COPY . /app/
WORKDIR /app/

ENV DOCKER_HOST unix:///var/run/docker.sock

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["forego", "start", "-r"]
