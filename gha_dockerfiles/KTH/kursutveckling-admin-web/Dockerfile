FROM kthse/kth-nodejs:14.0.0

RUN mkdir -p /npm && \
    mkdir -p /application

# We do this to avoid npm install when we're only changing code
WORKDIR /npm

COPY ["package.json", "package.json"]
COPY ["package-lock.json", "package-lock.json"]

RUN npm install --production --no-optional

# Add the code and copy over the node_modules-catalog
WORKDIR /application
RUN cp -a /npm/node_modules /application && \
    rm -rf /npm

# Copy files.
COPY ["config", "config"]
COPY ["public", "public"]
COPY ["i18n", "i18n"]
COPY [".babelrc", ".babelrc"]
COPY [".eslintrc", ".eslintrc"]
COPY ["package.json", "package.json"]
RUN npm run docker

# Copy source files.
COPY ["app.js", "app.js"]
COPY ["server", "server"]

ENV NODE_PATH /application

EXPOSE 3000

CMD ["node", "app.js"]
