FROM node:12
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils 2>&1 \
    #
    # Verify git and needed tools are installed
    && apt-get install -y git procps git-flow \
    #
    # Remove outdated yarn from /opt and install via package
    # so it can be easily updated via apt-get upgrade yarn
    && rm -rf /opt/yarn-* \
    && rm -f /usr/local/bin/yarn \
    && rm -f /usr/local/bin/yarnpkg \
    && apt-get install -y curl apt-transport-https lsb-release \
    && curl -sS https://dl.yarnpkg.com/$(lsb_release -is | tr '[:upper:]' '[:lower:]')/pubkey.gpg | apt-key add - 2>/dev/null \
    && echo "deb https://dl.yarnpkg.com/$(lsb_release -is | tr '[:upper:]' '[:lower:]')/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get -y install --no-install-recommends yarn \
    #
    # Install eslint globally
    && npm install -g eslint \
    #
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && npm install -g npm

ENV \
    # Switch back to dialog for any ad-hoc use of apt-get
    DEBIAN_FRONTEND=dialog \
    GATSBY_TELEMETRY_DEBUG=0 \
    # Setting opt-in to Gatsby telemetry
    GATSBY_TELEMETRY_DISABLED=0 \
    # Setting Node environment...
    NODE_ENV=development \
    # Setting Node loglevel...
    NPM_CONFIG_LOGLEVEL=warn \
    # Setting Node modules path...
    PATH=/usr/src/app/node_modules/.bin:$PATH

# Creating app directory
RUN \
    mkdir -p /usr/src/app && \
    mkdir -p /usr/src/app/node_modules && \
    chown -R node:node /usr/src/app

# Setting as working directory
# Using -p because mkdir isn't recursive by default
WORKDIR /usr/src/app

# Copy app package manifest...
COPY package*.json ./

# Install dependencies
RUN npm install

# Bundle app source files and set app directory permissions
COPY --chown=node:node . .

# Set user to node
# USER node

# Port :8000 will be published on runtime
EXPOSE 8000

# Starting app...
CMD ["npm","start"]
