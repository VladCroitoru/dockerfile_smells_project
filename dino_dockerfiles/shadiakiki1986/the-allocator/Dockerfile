FROM nginx:alpine
MAINTAINER Shadi Akiki

RUN apk add --update --no-cache make vim nodejs
WORKDIR /usr/share/the-allocator
COPY etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY . .
RUN npm install -g bower && make install

# WORKDIR /usr/share/nginx/html/

