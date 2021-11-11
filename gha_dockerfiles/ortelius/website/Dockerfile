# base nginx image
FROM node:lts-alpine3.13 as build

# an arbitrary directory to build our site in
WORKDIR /build
ENV HUGO_ENV=production

# the copy and build the site
COPY . .

# install node_modules, will be cached unless package.json has changed
RUN npm ci; \
  apk add --update hugo git; \
  /usr/bin/hugo

FROM wernight/alpine-nginx-pagespeed

# copy public/ from the 'build' container into the nginx container
COPY --from=build /build/public /etc/nginx/html

# Configure pagespeed
COPY --from=build /build/conf/pagespeed.conf /etc/nginx/
COPY --from=build /build/conf/nginx.conf /etc/nginx/

# fix /tmp/pagespeed_cache permission denied
RUN mkdir -p /tmp/pagespeed_cache; \
    chmod a+w /tmp/pagespeed_cache; 
