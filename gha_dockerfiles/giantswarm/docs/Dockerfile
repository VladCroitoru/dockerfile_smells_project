FROM quay.io/giantswarm/hugo:v0.88.1 AS build

RUN apk --no-cache add findutils gzip

WORKDIR /docs

COPY . /docs

RUN hugo \
      --verbose \
      --gc \
      --minify \
      --source src \
      --path-warnings \
      --destination /public \
      --cleanDestinationDir

# Compress static files above 512 bytes using gzip
RUN find /public \
  -type f -regextype posix-extended \
  -size +512c \
  -iregex '.*\.(css|csv|html?|js|svg|txt|xml|json|webmanifest|ttf)' \
  -exec gzip -9 -k '{}' \;

FROM quay.io/giantswarm/nginx:1.21-alpine

COPY nginx.conf /etc/nginx/nginx.conf

RUN rm /docker-entrypoint.d/* && \
  sed -i \
    -e 's|listen       80;|listen 8080;|' \
    -e 's|listen  [::]:80;||' \
    /etc/nginx/conf.d/default.conf

RUN nginx -t -c /etc/nginx/nginx.conf && \
    rm -rf /tmp/nginx.pid

EXPOSE 8080

COPY --from=build --chown=101 /public /usr/share/nginx/html
