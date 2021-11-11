FROM node:12-alpine

COPY / /home/node/
WORKDIR /home/node

RUN apk add --no-cache tini \
&& npm install --global http-server \
&& npm ci --silent \
&& npm run build-lib \
&& npm run build-testapp \
&& npm run build-elements \
&& npx compodoc \
&& sed -i 's#REPLACE_ME#/journey-maps-client-elements/#' dist/journey-maps-client-elements/index.html \
&& mv dist/documentation dist/journey-maps-client-testapp \
&& mv dist/journey-maps-client-elements dist/journey-maps-client-testapp \
&& rm -rf node_modules

EXPOSE 8080

USER node
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["http-server", "dist/journey-maps-client-testapp"]
