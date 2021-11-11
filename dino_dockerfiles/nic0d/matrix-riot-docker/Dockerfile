FROM alpine:3.4

# Git branch to download
ENV BV_VEC=0.9.5

# To rebuild the image, add `--build-arg REBUILD=$(date)` to your docker build
# command.
ARG REBUILD=0

# update and upgrade
# installing riot.im with nodejs/npm
RUN apk update \
    && apk add \
        curl \
        git \
        libevent \
        libffi \
        libjpeg-turbo \
        libssl1.0 \
        nodejs \
        sqlite-libs \
        unzip \
        ; \
    npm install -g webpack http-server \
    && curl -L https://github.com/vector-im/riot-web/archive/v$BV_VEC.zip -o v.zip \
    && unzip v.zip \
    && rm v.zip \
    && mv riot-web-$BV_VEC riot-web \
    && cd riot-web \
    && npm install \
    && rm -rf /riot-web/node_modules/phantomjs-prebuilt/phantomjs \
    && GIT_VEC=$(git ls-remote https://github.com/vector-im/riot-web $BV_VEC | cut -f 1) \
    && echo "riot:  $BV_VEC ($GIT_VEC)" > /synapse.version \
    && npm run build \
    ; \
    apk del \
        git \
        unzip \
        ; \
    rm -rf /var/lib/apk/* /var/cache/apk/*

# install homeserver template
COPY adds/start.sh /start.sh
COPY adds/config.json /riot-web/webapp/config.json

RUN chmod a+x /start.sh

# startup configuration
ENTRYPOINT ["/start.sh"]
