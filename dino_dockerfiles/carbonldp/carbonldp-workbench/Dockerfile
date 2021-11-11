# === START: Stage #1 - BUILD
FROM node:10.12.0-alpine AS builder

WORKDIR /usr/app

# Wildcard to copy package-lock.json too
COPY package*.json ./

RUN npm install

# Copy only the required files/folders ordered from least o most subject to change
# That way the built will only run if any of these files/folders are modified
COPY angular.json .
COPY ngsw-config.json .
COPY tsconfig.json .
COPY tslint.json .
COPY e2e e2e
COPY src src
COPY typings typings

RUN npm run-script build
# === END: Stage #1 - BUILD

# === START: Stage #2 - APP
FROM nginx:1.15.5-alpine

COPY server/nginx.conf /etc/nginx/nginx.conf
COPY scripts/write-global-variables.sh /opt/

COPY --from=builder /usr/app/dist/app /usr/share/nginx/html/

EXPOSE 80

ENTRYPOINT [ "/bin/sh", "-c", "/opt/write-global-variables.sh /usr/share/nginx/html/index.html && nginx -g 'daemon off;'" ]
