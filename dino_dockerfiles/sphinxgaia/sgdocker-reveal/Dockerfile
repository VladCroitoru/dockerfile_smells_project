FROM node:6.12.3-alpine


# npm loglevel in base image is verbose, adjust to warnings only
ENV NPM_CONFIG_LOGLEVEL warn

# Set environment variables for reveal.js GitHub repo
ENV VERSION=3.6 \
  VCS=https://github.com \
  GITUSER=Sphinxgaia \
  REPO=my_reveal


RUN set -ex \
    && apk add --no-cache tini \
    && apk add --no-cache --virtual .fetch-deps \
        ca-certificates \
        tar \
        wget \
    && apk add --no-cache --virtual .build-deps \
        g++ \
        make \
        python

RUN wget -qO /tmp/reveal.js.tar.gz $VCS/$GITUSER/$REPO/archive/$VERSION.tar.gz \
    && tar -xzf /tmp/reveal.js.tar.gz -C / \
    && rm -f /tmp/reveal.js.tar.gz \
    && mv $REPO-$VERSION reveal.js

RUN mkdir -p /reveal.js/node_modules \
    && npm install -g grunt-cli \
    && npm install --prefix /reveal.js \
    && npm cache clean \
    && rm -rf /root/.node-gyp /tmp/npm* /tmp/phantomjs \
    && apk del .fetch-deps \
    && apk del .build-deps \
    && chown -R node:node /reveal.js

WORKDIR /reveal.js

USER node

EXPOSE 8000

ENTRYPOINT ["tini", "--"]
CMD ["grunt", "serve"]
