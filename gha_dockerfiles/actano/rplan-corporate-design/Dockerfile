FROM node:12 as install
ARG NPM_TOKEN

WORKDIR /build

RUN echo "//registry.npmjs.org/:_authToken=\${NPM_TOKEN}" > ~/.npmrc

COPY yarn.lock yarn.lock
COPY package.json package.json
RUN yarn install --frozen-lockfile

FROM node:12 as build

WORKDIR /build

COPY --from=install /build/node_modules /build/node_modules
COPY --from=install /build/package.json /build
COPY --from=install /build/yarn.lock /build

COPY tsconfig.json tsconfig.json
COPY assets assets
COPY storybook storybook
COPY src src
COPY static static

RUN yarn build-storybook

FROM nginx:alpine as webserver

COPY storybook/webserver/nginx.conf /etc/nginx
COPY --from=build /build/storybook-static /html

ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
