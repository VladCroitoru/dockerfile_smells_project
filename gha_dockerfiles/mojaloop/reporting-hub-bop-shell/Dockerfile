FROM node:lts-alpine as builder
WORKDIR /opt/reporting-hub-bop-shell
ENV PATH /opt/reporting-hub-bop-shell/node_modules/.bin:$PATH

# Install build dependencies
RUN apk add --no-cache -t build-dependencies git make gcc g++ python libtool autoconf automake \
    && cd $(npm root -g)/npm \
    && npm config set unsafe-perm true \
    && npm install -g node-gyp

COPY package.json /opt/reporting-hub-bop-shell/
COPY yarn.lock /opt/reporting-hub-bop-shell/
RUN yarn --frozen-lockfile

COPY ./ /opt/reporting-hub-bop-shell/

# Adds the package version and commit hash
ARG REACT_APP_VERSION
ENV REACT_APP_VERSION=$REACT_APP_VERSION

ARG REACT_APP_COMMIT
ENV REACT_APP_COMMIT=$REACT_APP_COMMIT

# Build production application files
RUN yarn build

# Second part, create a config at boostrap via entrypoint and and serve it
FROM nginx:1.16.0-alpine

# JQ is used to convert from JSON string to json file in bash
# Required for runtime configuration scripts
RUN apk add --no-cache jq

# Create user with uid 1001. Mojaloop helm templates default to uid 1001 for
# running containers as non-root for better security
RUN addgroup -g 1001 appuser && \
    adduser -S -u 1001 -g appuser appuser

# Give user permission to clean up ngnix configuration files
RUN chown -R appuser:appuser /etc/nginx
WORKDIR /usr/share/nginx/html

# Copy build over from builder
COPY --from=builder /opt/reporting-hub-bop-shell/dist/ /usr/share/nginx/html

# Remove nginx config
RUN rm /etc/nginx/conf.d/default.conf /etc/nginx/nginx.conf

# Copy over local config and script
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/start.sh /usr/share/nginx/start.sh

# Copy over scripts that enable runtime configuration
COPY docker/entrypoint.sh /usr/share/nginx/html/entrypoint.sh
COPY docker/createJSONConfig.sh /usr/share/nginx/html/createJSONConfig.sh
COPY docker/createRemoteConfig.sh /usr/share/nginx/html/createRemoteConfig.sh
COPY docker/loadRuntimeConfig.sh /usr/share/nginx/html/loadRuntimeConfig.sh

# Give appuser permissions to nginx
RUN chown -R appuser:appuser \
    /usr/share/nginx \
    /var/cache/nginx \
    /var/run/

# Make scripts executable
RUN chmod +x /usr/share/nginx/html/entrypoint.sh
RUN chmod +x /usr/share/nginx/html/createJSONConfig.sh
RUN chmod +x /usr/share/nginx/html/createRemoteConfig.sh
RUN chmod +x /usr/share/nginx/html/loadRuntimeConfig.sh

USER appuser
EXPOSE 8080
ENTRYPOINT ["/usr/share/nginx/html/entrypoint.sh"]
CMD ["sh", "/usr/share/nginx/start.sh"]
# TODO: Need to add 8080 to image-scan whitelist
#       Investigate Feed data unavailable, cannot perform CVE scan for distro: alpine:3.14.2
