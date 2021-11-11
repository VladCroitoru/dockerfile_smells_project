FROM node:alpine3.12 AS webui

WORKDIR /build
ADD webui/package.json webui/package-lock.json ./
RUN npm i
ADD webui ./
RUN npm run build


FROM node:alpine3.12 AS core

WORKDIR /build
ADD package.json package-lock.json ./
RUN npm i
ADD src tsconfig.json ./
RUN npm run build
RUN npm prune --production

FROM node:alpine3.12

RUN apk add --no-cache restic tzdata \
    && restic self-update \
    && mkdir /var/cache/restic \
    && chmod 1777 /var/cache/restic
WORKDIR /app
COPY --from=core /build/dist ./
COPY --from=core /build/node_modules node_modules
COPY --from=webui /build/dist webui
VOLUME /var/cache/restic
USER nobody
CMD node .
