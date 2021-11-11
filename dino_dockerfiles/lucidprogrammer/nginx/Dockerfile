FROM nginx:1.12.0-alpine
LABEL maintainer "Lucid Programmer<lucidprogrammer@hotmail.com>"
RUN apk add --no-cache jq
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf
COPY default-ssl.conf /etc/nginx/conf.d/default-ssl.template
# keep an ssl folder already created
RUN mkdir -p /etc/nginx/ssl/

# keep a folder for proxies configuration json file - expects proxies.json
RUN mkdir -p /etc/nginx/conf.d/proxies
# keep a folder for locations configuration
RUN mkdir -p /etc/nginx/conf.d/locations
# keep a folder for upstream configurations
RUN mkdir -p /etc/nginx/conf.d/upstream

# copy the sample json file for info
COPY proxies.sample.json /etc/nginx/conf.d/proxies/proxies.json.sample
# copy the default as a sample, if there is no proxies.json in /proxies folder we will convert this to default.conf
COPY location.default.conf /etc/nginx/conf.d/locations/default.sample
COPY location.proxy.basic /etc/nginx/conf.d/locations/proxy.basic
COPY location.proxy.websockets /etc/nginx/conf.d/locations/proxy.websockets

COPY entrypoint.sh /entrypoint.sh

RUN addgroup -g 1000 -S www-data \
 && adduser -u 1000 -D -S -G www-data www-data

ENTRYPOINT ["/entrypoint.sh"]
