# Stage 1 (build)
# base image
FROM quay.io/ebi-ait/ingest-base-images:node_12.16.3-alpine as build-step

# set working directory
RUN mkdir /app
WORKDIR /app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY ./package.json /app/package.json
COPY ./yarn.lock /app/yarn.lock
COPY ./.snyk /app/.snyk
RUN yarn install --frozen-lockfile

# add app and build dependencies
COPY ./angular.json /app/angular.json
COPY ./browserslist /app/browserslist
COPY ./tsconfig.json /app/tsconfig.json
COPY ./src /app/src

# build app
RUN ng build -c=env

# Stage 2 (serve)
FROM quay.io/ebi-ait/ingest-base-images:nginx_1.19.3-alpine

COPY --from=build-step /app/dist /usr/share/nginx/html
COPY ./docker-assets/nginx.conf /etc/nginx/conf.d/default.conf

COPY ./docker-assets/prepare_artifact.sh /usr/share/nginx/prepare_artifact.sh
RUN chmod +x /usr/share/nginx/prepare_artifact.sh

# Run on 4200 just so we don't have to change helm config files
EXPOSE 4200
CMD ["sh", "-c", "/usr/share/nginx/prepare_artifact.sh && nginx -g 'daemon off;'"]
