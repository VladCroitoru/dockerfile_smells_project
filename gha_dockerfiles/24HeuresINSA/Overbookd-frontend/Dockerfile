FROM node:15.3.0-alpine3.10

WORKDIR /Overbookd/frontend
ARG BASE_URL_KEYCLOAK
ARG BASE_URL

ENV BASE_URL=$BASE_URL
ENV BASE_URL_KEYCLOAK=$BASE_URL_KEYCLOAK

COPY . .

RUN npm ci\
    && npm run build\
    && find . -maxdepth 1 ! -name 'dist' -type f -exec rm -r {} +\
    && find . -maxdepth 1 ! -name 'dist' ! -name '.' ! -name '..' -type d -exec rm -r {} +\
    && npm install serve


EXPOSE 1234

CMD ["./node_modules/.bin/serve", "--single", "--listen", "1234", "dist"]