FROM mhart/alpine-node:6.11

ENV ADDITIONAL_PKGS="make g++ python nasm autoconf automake zlib-dev git"

WORKDIR /var/www

RUN npm update -g npm && \
  npm install -g grunt-cli

RUN apk add --no-cache openssl && \
  wget -O - https://github.com/codeforchiba/feschibal/tarball/develop | tar xz && \
  mv $(ls -1) feschibal && \
  apk del openssl

WORKDIR feschibal

RUN apk add --no-cache ${ADDITIONAL_PKGS} && \
  npm install --unsafe-perm && \
  grunt build && \
  apk del ${ADDITIONAL_PKGS} && \
  rm -rf /tmp/npm* /var/cache/apk/* /root/.npm /root/.node-gyp node_modules

EXPOSE 9000

RUN npm install --only=production

CMD ["npm", "start"]
