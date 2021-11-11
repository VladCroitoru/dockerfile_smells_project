FROM mhart/alpine-node

ENV PATH=$PATH:/usr/src/node_modules/.bin
ARG NODE_ENV=production

# Install app
ENV NODE_ENV=$NODE_ENV
ENV NODE_PATH=/usr/src/build
ADD package.json /tmp/
RUN cd /tmp && \
    npm install && \
    rm -rf /root/.npm && \
    mkdir -p /usr/src && \
    ln -sf /tmp/node_modules /usr/src/node_modules && \
    ln -sf /tmp/package.json /usr/src/package.json

# Add source
WORKDIR /usr/src
COPY index.js /usr/src

# Default command
CMD [ "npm", "start" ]
