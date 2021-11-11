# build the js app
FROM node:10.0.0 as build-deps
WORKDIR /app/
COPY ./package.json /app/
RUN npm install
COPY . /app
RUN npm install
RUN npm run build:config
RUN npm run build:css
RUN npm run mapping
RUN npm run install:bower --unsafe-perm

# use the ngnix server to serve the built stuff
FROM nginx:1.13.12

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=build-deps /app/index.html /app/index.html
COPY --from=build-deps /app/js /app/js
COPY --from=build-deps /app/css /app/css
COPY --from=build-deps /app/html /app/html
COPY --from=build-deps /app/node_modules/requirejs-text/text.js /app/node_modules/requirejs-text/text.js
COPY --from=build-deps /app/node_modules/requirejs-json/json.js /app/node_modules/requirejs-json/json.js
COPY --from=build-deps /app/favicon.png /app/favicon.png
COPY --from=build-deps /app/img /app/img
COPY --from=build-deps /app/fonts /app/fonts

RUN echo '{ \
  "httpPort": 80, \
  "configPath": "/app/js/parameters.js", \
  "configType": "text", \
  "dataPath":   "/app" \
}' > /etc/ezmaster.json
