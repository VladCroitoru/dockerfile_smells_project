FROM node:16.8.0 as build

# Environment.
WORKDIR /app
COPY ./jsconfig.json ./jsconfig.json
COPY ./package*.json ./
RUN npm install

# Build.
COPY ./public ./public
COPY ./src ./src
RUN npm run build


# React app could be served without node.
FROM nginx:stable

# App.
COPY --from=build /app/build /usr/share/nginx/html

# This commad setup API_URL.
CMD sed -i "s%index  index.html index.htm;%try_files \$uri /index.html;%g" "/etc/nginx/conf.d/default.conf" && \
    sed -i "s%API_URL_PLACEHOLDER%${REACT_APP_API_URL}%g" "/usr/share/nginx/html/index.html" && \
    nginx -g "daemon off;"
