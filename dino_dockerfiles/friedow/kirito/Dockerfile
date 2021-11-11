FROM node:alpine AS builder
WORKDIR /usr/src/kirito
COPY . .
RUN npm install && \
    npm run build && \
    mkdir ./builder && \
    mv ./build ./builder/build && \
    mv ./tsconfig.json ./builder/tsconfig.json && \
    mv ./package.json ./builder/package.json && \
    mv ./src/interface ./builder/build/interface

FROM zenato/puppeteer
USER root
COPY --from=builder /usr/src/kirito/builder .
RUN npm install --production && \
    chown -R pptruser:pptruser /build
USER pptruser
CMD npm run production
