FROM node:14.17.3-alpine3.14 as sdk

ENV CI=true NPM_CONFIG_LOGLEVEL=error GENERATE_SOURCEMAP=false INLINE_RUNTIME_CHUNK=false

WORKDIR /app

COPY package*.json /app/

RUN npm install

COPY . .

RUN npm run test

RUN npm run build
RUN for f in `find build -type f -name '*.html' -o -name '*.ico' -o -name '*.css' -o -name '*.js' -o -name '*.json' -o -name '*.txt' -o -name '*.svg'`; \
    do gzip -9c "$f">"$f.gz"; \
  done

FROM nginx:alpine as runtime

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/conf.d/frontend.conf /etc/nginx/conf.d/frontend.conf
COPY nginx/conf.d/headers.conf /etc/nginx/conf.d/headers.conf

COPY --from=sdk /app/build/ /usr/share/nginx/html

