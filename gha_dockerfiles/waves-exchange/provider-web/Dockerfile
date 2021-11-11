FROM node:15-alpine AS build
COPY . /app/
WORKDIR /app
RUN npm ci
RUN node ./node_modules/esbuild/install.js
WORKDIR /app/packages/provider-web-ui
RUN npm run build

FROM nginx:1.17-alpine
WORKDIR /iframe-entry
COPY nginx/webkeeper.conf /etc/nginx/conf.d/webkeeper.conf
COPY --from=build /app/packages/provider-web-ui/dist/ /iframe-entry/signer/
EXPOSE 80
