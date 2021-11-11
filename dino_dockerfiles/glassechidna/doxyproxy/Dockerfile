FROM openresty/openresty:1.11.2.2-alpine

RUN apk add --update perl curl
RUN /usr/local/openresty/bin/opm get pintsized/lua-resty-http

EXPOSE 8080

COPY ./nginx/conf /usr/local/openresty/nginx/conf
COPY ./nginx/lualib /usr/local/openresty/nginx/lualib
COPY ./nginx/sites-enabled /usr/local/openresty/nginx/sites-enabled
