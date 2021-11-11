FROM node:12.18.2-alpine

RUN apk --no-cache add g++ gcc libgcc libstdc++ linux-headers make python jq
RUN npm install --quiet node-gyp -g

ARG NODE_ENV

ARG SENTRY_RELEASE

ENV NODE_ENV ${NODE_ENV:-dev}

RUN mkdir app

WORKDIR /app

ADD package*.json /app/

RUN apk add --update --no-cache \
    make \
    g++ \
    jpeg-dev \
    cairo-dev \
    giflib-dev \
    pango-dev \
    msttcorefonts-installer fontconfig \
    font-noto \
    font-noto-adlam \
    font-noto-adlamunjoined \
    font-noto-arabic \
    font-noto-armenian \
    font-noto-avestan \
    font-noto-bamum \
    font-noto-bengali \
    font-noto-buhid \
    font-noto-carian \
    font-noto-chakma \
    font-noto-cherokee \
    font-noto-cypriot \
    font-noto-deseret \
    font-noto-devanagari \
    font-noto-ethiopic \
    font-noto-extra \
    font-noto-georgian \
    font-noto-glagolitic \
    font-noto-gothic \
    font-noto-gujarati \
    font-noto-gurmukhi \
    font-noto-hebrew \
    font-noto-kannada \
    font-noto-kayahli \
    font-noto-khmer \
    font-noto-lao \
    font-noto-lisu \
    font-noto-malayalam \
    font-noto-mandaic \
    font-noto-myanmar \
    font-noto-nko \
    font-noto-olchiki \
    font-noto-oldturkic \
    font-noto-oriya \
    font-noto-osage \
    font-noto-osmanya \
    font-noto-shavian \
    font-noto-sinhala \
    font-noto-tamil \
    font-noto-telugu \
    font-noto-thaana \
    font-noto-thai \
    font-noto-tibetan \
    font-noto-tifinagh \
    font-noto-vai \
    terminus-font \
    ttf-opensans \
    font-bakoma \
    font-misc-misc \
    font-croscore

RUN fc-cache -f && rm -rf /var/cache/*

RUN npm i canvas --build-from-source

RUN npm install

ADD dist /app/dist/

EXPOSE 8080

CMD npm run start:${NODE_ENV} | grep -v ELB-HealthCheckÍer
