FROM node:9.5.0-alpine
LABEL maintainer="esplo@users.noreply.github.com"

# add external library (from https://github.com/znly/docker-protobuf)
RUN apk add --update \
    && apk add --no-cache protobuf curl \
    && mkdir -p /protobuf/google/protobuf \
    && for f in any duration descriptor empty struct timestamp wrappers; do \
         curl -L -o /protobuf/google/protobuf/${f}.proto https://raw.githubusercontent.com/google/protobuf/master/src/google/protobuf/${f}.proto; \
       done \
    && apk del curl \
    && rm -rf /var/cache/apk/*

COPY package.json ./
RUN npm i --verbose

CMD [ \
  "./node_modules/.bin/chokidar", \
  "/src/*.proto", \
  "-c", \
  "protoc \
    --plugin=protoc-gen-ts=./node_modules/.bin/protoc-gen-ts \
    --js_out=import_style=commonjs,binary:/dist \
    --ts_out=service=true:/dist \
    -I /src \
    -I /protobuf \
    /src/*.proto" \
]
