FROM nginx:alpine

LABEL maintainer="Harvey Chow <harvey@hcdesigns.nl>"

COPY includes /etc/nginx/includes
COPY nginx.conf /etc/nginx/
COPY sites /etc/nginx/conf.d

COPY html /var/www/html

RUN apk update \
    && apk upgrade \
    && apk add --no-cache bash \
    && adduser -D -H -u 1000 -s /bin/bash www-data

# EXPOSE 80 443 # ALREADY SET IN PARENT DOCKERFILE
# CMD ["nginx"] # ALREADY SET IN PARENT DOCKERFILE

WORKDIR /etc/nginx