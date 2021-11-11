FROM node:16.8.0 AS ui-build
WORKDIR /usr/src/app
COPY demofrontend/ ./demofrontend/
RUN cd demofrontend && npm install && npm run build


FROM nginx:alpine

#!/bin/sh

COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf

## Remove default nginx index page
RUN rm -rf /usr/share/nginx/html/*

# Copy from the stahg 1
COPY --from=ui-build /usr/src/app/demofrontend/build/ /usr/share/nginx/html

EXPOSE 4200 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]
