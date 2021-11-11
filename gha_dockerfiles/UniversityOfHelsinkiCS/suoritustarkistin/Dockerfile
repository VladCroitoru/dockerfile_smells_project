FROM node:14.17

# Set timezone to Europe/Helsinki
RUN echo "Europe/Helsinki" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

ARG BASE_PATH
ENV BASE_PATH=$BASE_PATH
ARG NODE_ENV
ENV NODE_ENV=$NODE_ENV

RUN echo "${NODE_ENV}"

# Setup
WORKDIR /usr/src/app
COPY package* ./

RUN npm ci --only=production

# Install Sentry
RUN curl -sL https://sentry.io/get-cli/ | bash

COPY . .
RUN SENTRY_RELEASE=$(sentry-cli releases propose-version) && \
    echo "${SENTRY_RELEASE}" > /SENTRY_RELEASE && \
    SENTRY_RELEASE="${SENTRY_RELEASE}" npm run build

CMD ["npm", "start"]