# dekobon/consul-visualizer:latest
FROM alpine:3.2

MAINTAINER Elijah Zupancic <elijah@zupancic.name>

ENV CONSUL_SERVERS 165.225.168.222:8500
ENV APP_PORT 3000
ENV CONTAINERBUDDY file:///opt/containerbuddy/app.json
ENV CONTAINERBUDDY_VERSION 0.0.4
ENV CONTAINERBUDDY_CHECKSUM 81ce46308eff9b7e9f8865f92805c33fcba2fc47
ENV CONSUL_TEMPLATE_VERSION 0.12.0
ENV CONSUL_TEMPLATE_CHECKSUM 1fff23fa44fd0af0cb56f011a911af1e9d407a2eeb360f520a503d2f330fdf43

# Add custom scripts directory
ADD usr /usr

# Add nodejs application
ADD ui /app

# Remove the package list cache from the system because
# we don't need that bloating the image
RUN apk update && \
    apk upgrade && \
    apk add curl bash nodejs grep jq git drill && \
    rm -rf /var/cache/apk/*

# We ditch the default grep in favor of GNU grep because
# we need to do more advanced matching
RUN rm -f /bin/grep && \
    ln -s /usr/bin/grep /bin/grep

# We set the executable bit on all of the newly added scripts
RUN find /usr/local/bin -type f | xargs chmod +x $1

# Upgrade NPM / bower to the latest version
RUN npm install -g npm bower && \
    npm install -g json

# Install NPM modules for the application
RUN npm install /app

# Add Bower directory
RUN mkdir -p /app/bower_components

# Add user that will be running the application
RUN adduser -h /app -s /bin/bash -D -u 1337 node

# Change ownership of the application to the runtime user
RUN chown -R node:node /app

# Install client javascript libraries
RUN chmod +wx /app/bower_components && \
    su node -c 'cd /app && bower install /app' && \
    chmod -R -w /app/bower_components

# Add Containerbuddy
RUN wget -q -O /tmp/containerbuddy.tar.gz "https://github.com/joyent/containerbuddy/releases/download/${CONTAINERBUDDY_VERSION}/containerbuddy-${CONTAINERBUDDY_VERSION}.tar.gz" && \
    echo "${CONTAINERBUDDY_CHECKSUM}  /tmp/containerbuddy.tar.gz" | sha1sum -c && \
    tar xzf /tmp/containerbuddy.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/containerbuddy && \
    rm /tmp/containerbuddy.tar.gz

# Add Consul Template
RUN wget -q -O /tmp/consul-template.zip "https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" && \
    echo "${CONSUL_TEMPLATE_CHECKSUM}  /tmp/consul-template.zip" | sha256sum -c && \
    unzip /tmp/consul-template.zip -d /tmp && \
    mv /tmp/consul-template /usr/local/bin && \
    chmod +x /usr/local/bin/consul-template && \
    rm /tmp/consul-template.zip

ADD opt /opt

RUN chmod +x /opt/containerbuddy/reload-app.sh

USER node

CMD [ "containerbuddy" "'node /app'" ]
