FROM nginx:alpine
MAINTAINER Adrien M amaurel90@gmail.com

ENV DEBUG=false RAP_DEBUG="info" 
ARG VERSION_RANCHER_GEN="artifacts/master"

RUN apk add --no-cache nano ca-certificates unzip wget certbot bash openssl

# Install Forego & Rancher-Gen-RAP
ADD bin/ /usr/local/bin/

RUN chmod +x /usr/local/bin/rancher-gen \
	&& chmod u+x /usr/local/bin/forego \
	&& rm -f /tmp/rancher-gen-rap.zip
	
#Copying all templates and script	
COPY /app/ /app/
WORKDIR /app/

# Seting up repertories & Configure Nginx and apply fix for very long server names
RUN chmod +x /app/letsencrypt.sh \
    && mkdir -p /etc/nginx/certs /etc/nginx/vhost.d /etc/nginx/conf.d /usr/share/nginx/html /etc/letsencrypt \
    && echo "daemon off;" >> /etc/nginx/nginx.conf \
    && sed -i 's/^http {/&\n    server_names_hash_bucket_size 128;/g' /etc/nginx/nginx.conf \
    && chmod u+x /app/remove 

ADD proxy.conf /etc/nginx/proxy.conf

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh" ]
CMD ["forego", "start", "-r"]
