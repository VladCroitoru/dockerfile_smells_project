#
# Build the website
#
FROM node:10.0-slim AS witc-build

COPY ./site /build
WORKDIR /build
RUN mkdir -p fonts && wget http://www.figlet.org/fonts/doh.flf -O fonts/Standard.flf
RUN npm install

#
# Build the webserver
#

FROM nginx:1.14

# Generate localhost self-signed cert (it's safe to sore it inside the image because it's just localhost)
RUN apt-get update && \
    apt-get install -y openssl && \
    apt-get clean && rm -rf /var/cache/apt/*.bin

RUN bash -c 'openssl req -x509 -out /etc/ssl/certs/localhost.crt -keyout /etc/ssl/private/localhost.key \
  -newkey rsa:2048 -nodes -sha256 \
  -subj "/CN=localhost" -extensions EXT -config <( \
   printf "[dn]\\nCN=localhost\\n[req]\\ndistinguished_name = dn\\n[EXT]\\nsubjectAltName=DNS:localhost\\nkeyUsage=digitalSignature\\nextendedKeyUsage=serverAuth")'

# Configure nginx
COPY nginx-default.conf /etc/nginx/conf.d/default.conf

# Copy required webapp files (no sofisticated build using ie. Webpack, I'm too lazy)
COPY --from=witc-build /build/fonts /var/www/html/fonts/
COPY --from=witc-build \
    /build/index.html \
    /build/node_modules/figlet/lib/figlet.js \
    /var/www/html/
