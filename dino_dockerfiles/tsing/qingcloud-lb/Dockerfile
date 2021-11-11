FROM node:7.6-alpine

RUN apk add --no-cache --virtual .build-deps tar curl && \
  curl -o- -L https://yarnpkg.com/install.sh | sh && \
  apk del .build-deps
ENV PATH /root/.yarn/bin:$PATH

WORKDIR /app/

COPY yarn.lock package.json /app/
RUN yarn --pure-lockfile --prod && yarn cache clean
COPY . /app/

ENV DEBUG=qingcloud-lb
ENTRYPOINT ["node", "main.js", "config.json"]
