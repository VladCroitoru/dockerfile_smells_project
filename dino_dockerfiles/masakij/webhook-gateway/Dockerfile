FROM node:6.11.4-alpine
MAINTAINER masakij

# Copy application files
COPY package.json yarn.lock /usr/src/app/
COPY ./src /usr/src/app/src
WORKDIR /usr/src/app

# Install Yarn and Node.js dependencies
RUN yarn install --production --no-progress && \
    yarn cache clean && \
    apk --update add --no-cache tini

ENTRYPOINT ["/sbin/tini", "--", "npm"]
CMD ["start"]
