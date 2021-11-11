FROM buildpack-deps:buster-curl

ENV REFRESHED_AT 2021-02-28

ENV NODE_VERSION 14.16.0
ENV YARN_VERSION 1.22.5
ENV NODE_ENV=production

RUN groupadd -r node && useradd -r -g node node

# gpg keys listed at https://github.com/nodejs/node
RUN set -ex \
  && for key in \
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
    56730D5401028683275BD23C23EFEFE93C4CFFFE \
  ; do \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
  done

RUN buildDeps='xz-utils apt-transport-https ca-certificates' \
  && set -x \
  && apt-get update && apt-get install -y $buildDeps --no-install-recommends \
  && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
  && apt-get update \
	&& apt-get install -y git \
  && curl -SLO "https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz" \
  && curl -SLO "https://nodejs.org/dist/v${NODE_VERSION}/SHASUMS256.txt.asc" \
  && grep " node-v${NODE_VERSION}-linux-x64.tar.xz\$" SHASUMS256.txt.asc | shasum -a 256 -c - \
  && tar -xJf "node-v${NODE_VERSION}-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v${NODE_VERSION}-linux-x64.tar.xz" SHASUMS256.txt.asc \
  && apt-get install -y yarn=${YARN_VERSION}-1 \
  && rm -rf /var/lib/apt/lists/* \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs \
  && yarn -V \
  && node -v

RUN yarn global add nodemon node-gyp

RUN curl -sSf -o /bin/wait-for-it.sh https://raw.githubusercontent.com/nikosch86/wait-for-it/master/wait-for-it.sh && chmod +x /bin/wait-for-it.sh

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

CMD [ "npm", "start" ]
