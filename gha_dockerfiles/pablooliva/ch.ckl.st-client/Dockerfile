FROM node:12.14.0-alpine3.11 as build-stage
WORKDIR /app
COPY . /app
RUN npm install
RUN npm install g @angular/cli@8.3.21
RUN npm link @angular/cli@8.3.21
# temporary fixes for failing builds
# ERROR in node_modules/@types/quill/node_modules/quill-delta/dist/Delta.d.ts(1,8): error TS1192:
# Module '"/app/node_modules/@types/quill/node_modules/fast-diff/diff"' has no default export.
COPY ./patches/diff.d.ts "/app/node_modules/@types/quill/node_modules/fast-diff/diff.d.ts"
COPY ./patches/Delta.d.ts "/app/node_modules/@types/quill/node_modules/quill-delta/dist/Delta.d.ts"
RUN npm run build

FROM nginx:1.15
COPY --from=build-stage /app/dist/ /usr/share/nginx/html
COPY --from=build-stage /app/nginx/nginx-custom.conf /etc/nginx/conf.d/default.conf
# COPY --from=build-stage /app/nginx/ssl.conf /etc/nginx/conf.d/ssl.conf
COPY --from=build-stage /app/nginx/mime.types /etc/nginx/conf.d/mime.types
RUN mkdir -p /etc/nginx/logs
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
