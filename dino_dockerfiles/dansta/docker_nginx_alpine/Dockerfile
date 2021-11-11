FROM gliderlabs/alpine:latest

LABEL maintainer=dansta

# Setup environment so we can build behind proxy
ARG http_proxy
ENV http_proxy ${http_proxy:-localhost:3128}
ARG https_proxy
ENV https_proxy ${https_proxy:-localhost:3128}
ARG all_proxy
ENV all_proxy ${all_proxy:-localhost:3128}
# Set env. replace right most column with values specific to your environment
ARG NGINX_USER
ENV NGINX_USER ${NGINX_USER:-somebodysomeone}
ARG NGINX_GROUP
ENV NGINX_GROUP ${NGINX_GROUP:-somebodysomeone}
ARG NGINX_WORKER_PROCESSES
ENV NGINX_WORKER_PROCESSES ${NGINX_WORKER_PROCESSES:-4}
ARG NGINX_HTTP_PORT
ENV NGINX_HTTP_PORT ${NGINX_HTTP_PORT:-80}
ARG NGINX_HTTPS_PORT
ENV NGINX_HTTPS_PORT ${NGINX_HTTPS_PORT:-443}
ARG NGINX_DOMAIN
ENV NGINX_DOMAIN ${NGINX_DOMAIN:-example.com}
ARG NGINX_WWWDOMAIN
ENV NGINX_WWWDOMAIN ${NGINX_WWWDOMAIN:-www.example.com}
ARG NGINX_SSL_PROTOCOLS
ENV NGINX_SSL_PROTOCOLS ${NGINX_SSL_PROTOCOLS:-TLSv1 TLSv1.1 TLSv1.2}
ARG NGINX_SSL_CIPHERS
ENV NGINX_SSL_CIPHERS ${NGINX_SSL_CIPHERS:-CHACHA20:HIGH:!aNULL:!MD5:!RC4:!DES:!3DES}

# Update cache and install packages
RUN apk update && apk --no-cache add nginx \
                       python3 \
                       curl

# Add user, do not add home
RUN adduser ${NGINX_USER} -D -H -s /usr/sbin/nologin

# Add our own config file and mime types
ADD files/nginx.conf /etc/nginx/nginx.conf
ADD files/mime.types /etc/nginx/conf/mime.types
# Replace params
ADD files/replace.py /usr/local/bin/replace_conf
RUN chmod u+x /usr/local/bin/replace_conf
RUN /usr/local/bin/replace_conf /etc/nginx/nginx.conf NGINX

# Permissions
RUN chown -R ${NGINX_USER}:${NGINX_GROUP} /etc/nginx/

# Add remote log directory volume and a directory from which we grab the web content
VOLUME /var/log/
VOLUME /usr/local/nginx/

# Delete packages we dont need after build
RUN apk del python3

# Document port and autoexpose
EXPOSE ${NGINX_HTTP_PORT}/tcp \
       ${NGINX_HTTPS_PORT}/tcp

# Test the config file before launch to avoid zombie containers
RUN /usr/sbin/nginx -T

# Check ourselves to know we are alive
HEALTHCHECK --interval=15s --timeout=3s CMD curl -x 127.0.0.1:80 || exit 1

# If we issue no docker run command
CMD ["nginx", "-g", "daemon off;"]
