# Use the alpine image so we have the smallest image possible
FROM nodesource/nsolid:alpine

# Create `app` group and user since the base nodesource image
# doesn't currently.
RUN addgroup -g 1000 app \
    && adduser -G app -u 1000 -h /app -D app

USER app
WORKDIR /app
# These commands will get executed in the context of the build for the
# application container image.
# NOTE: copy the package.json file first because if it hasn't changed
# the cache will not be invalidated and thus the COPY and npm install
# will not introduce a new layer.
ONBUILD COPY package.json /app/package.json
ONBUILD RUN npm install --production
ONBUILD COPY . /app
