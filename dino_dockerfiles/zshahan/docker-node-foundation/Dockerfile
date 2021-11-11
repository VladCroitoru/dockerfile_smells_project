
FROM node:9.2.0-alpine
RUN apk add --no-cache git
RUN apk --no-cache add --virtual native-deps \
  g++ gcc libgcc libstdc++ linux-headers \
  make python curl autoconf automake \
  file nasm zlib-dev && \
  npm install --quiet node-gyp -g && \
  npm install --quiet gulp-cli -g && \
  npm install --quiet bower -g && \
  curl -Lo package.json https://raw.githubusercontent.com/zurb/foundation-sites-template/master/package.json && \
  npm install --quiet && \
  apk del native-deps
