FROM nginx:alpine
MAINTAINER Phillip Stromberg <phillip@4stromberg.com>
LABEL Description="NGINX Reverse Proxy for Arbitrary Python App Port"
LABEL USAGE="Pass an upstream as an argument and get nginx to reverse proxy for it"

# get our access logs on standard out
RUN ln -sf /dev/stdout /var/log/nginx/access.log

# file will get substituted by sed on launch
COPY default.conf /etc/nginx/conf.d/default.conf

ARG PUBLIC_PORT=80
ENV PUBLIC_PORT=$PUBLIC_PORT
EXPOSE 80
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
