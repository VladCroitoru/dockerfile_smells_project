
FROM node:16-alpine AS my-app-build

WORKDIR /app
COPY . .

RUN npm ci  && npm run build:prod 

# stage 2
FROM nginx:alpine
COPY nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /usr/share/nginx/html
COPY --from=my-app-build /app/dist/mobsos-evaluation-center /usr/share/nginx/html
RUN dos2unix docker-entrypoint.sh
# When the container starts, replace the env.js with values from environment variables
CMD ["/bin/sh",  "-c",  "envsubst < /usr/share/nginx/html/assets/env.template.js > /usr/share/nginx/html/assets/env.js && exec nginx -g 'daemon off;' "]