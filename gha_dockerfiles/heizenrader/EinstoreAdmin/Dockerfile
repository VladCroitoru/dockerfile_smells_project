FROM node:11-alpine as builder

WORKDIR /src

COPY public        /src/public
COPY src           /src/src
COPY package.json  /src/package.json
COPY tsconfig.json /src/tsconfig.json
COPY yarn.lock     /src/yarn.lock

ENV REACT_APP_API_URL "$REACT_APP_API_URL"

RUN yarn install && \
	yarn build

# ------------------------------------------------------------------------------

FROM nginx:alpine

COPY --from=builder /src/build /src
COPY docker/nginx/nginx.vh.default.conf /etc/nginx/conf.d/default.conf
COPY docker/nginx/entrypoint.sh /usr/bin

RUN mv /src/index.html /src/index.html.raw && \
	chmod -R 755 /src && \
	chown -R nginx:nginx /src && \
	chmod +x /usr/bin/entrypoint.sh

ENTRYPOINT /usr/bin/entrypoint.sh
