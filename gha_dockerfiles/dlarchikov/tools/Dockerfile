FROM ubuntu:18.04

WORKDIR /app

RUN apt update \
    && apt install -y curl software-properties-common make gcc g++ \
    && curl -sL https://deb.nodesource.com/setup_13.x | bash - \
    && apt install -y nodejs \
    && add-apt-repository ppa:nginx/stable \
    && apt update \
    && apt install -y nginx \
    && nginx -v

COPY ./ /app

RUN npm install node-sass\
    && npm install \
    && node ./patch-webpack.js \
    && npm run ng build \
    && cp -r /app/dist/* /var/www/html \
    && rm -rf /app

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]
