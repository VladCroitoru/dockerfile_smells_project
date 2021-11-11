FROM node:7.4

WORKDIR /usr/app
CMD node index.js

# Install yarnpkg
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && \
    apt-get install -y yarn && \
    rm -rf /var/lib/apt/lists/*

RUN yarn global add jspm@beta

COPY lib /usr/app

RUN yarn install && \
    cd static && \
    yarn install && \
    jspm install

EXPOSE 443
