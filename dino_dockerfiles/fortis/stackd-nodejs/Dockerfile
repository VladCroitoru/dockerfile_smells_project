FROM alpine:3.4
MAINTAINER Alan Bondarchuk <imacoda@gmail.com>

RUN apk upgrade --update && apk add nodejs && \
  npm install -g npm && \
  apk del curl make gcc g++ python linux-headers paxctl gnupg libgcc libstdc++ && \

  # Install packages
  npm install && \
  npm install -g express-generator bower mocha sinon should assert grunt-cli gulp node-gyp && \

  # Remove unused
  rm -rf /etc/ssl /SHASUMS256.txt.asc /usr/include \
    /usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp /root/.gnupg \
    /usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc /usr/lib/node_modules/npm/html

# Create user www-data
RUN addgroup -g 82 -S www-data && \
	adduser -u 82 -D -S -G www-data www-data

# Create work dir
RUN mkdir -p /var/www/html && \
    chown -R www-data:www-data /var/www

WORKDIR /var/www/html
VOLUME /var/www/html
EXPOSE 8080

CMD ["npm", "start"]
