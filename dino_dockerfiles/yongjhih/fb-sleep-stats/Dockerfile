FROM node:latest

ENV FB_SLEEP_STATS_HOME /fb-sleep-stats
ADD . $FB_SLEEP_STATS_HOME
WORKDIR $FB_SLEEP_STATS_HOME

RUN npm install && \
    npm run webpack

ENV TINI_VERSION v0.9.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc /
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 0527A9B7 && \
    gpg --verify /tini.asc && \
    chmod a+x /tini

#ENV POLLING_INTERVAL 600
#ENV APP_ID 435522656639081
#ENV PORT 3000

# for envsubst
RUN apt-get update && \
    apt-get install -y --no-install-recommends gettext-base && \
    apt-get clean && \
    rm -fr /var/lib/apt/lists/*

ADD docker-entrypoint.sh /
ENTRYPOINT ["/tini", "--", "/docker-entrypoint.sh"]
CMD ["npm", "start"]
