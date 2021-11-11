FROM node:8.8-alpine
LABEL maintainer "root@mewm.org"

RUN apk add --no-cache python curl sudo

WORKDIR /src
ADD . /src
RUN yarn install --production

ENTRYPOINT []
CMD ["node", "-v"]

