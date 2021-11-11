FROM node:8-alpine
MAINTAINER butlerx <butlerx@notthe.cloud>
ENV NODE_ENV=production
ARG DEP_VERSION=latest
RUN apk add --update git python build-base postgresql-client openssl && \
    mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN yarn && \
    yarn add cp-translations@latest && \
    apk del build-base python && \
    rm -rf /tmp/* /root/.npm /root/.node-gyp
EXPOSE 10301
CMD ["yarn", "start"]
