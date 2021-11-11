FROM vasdvp/lighthouse-node-application-base:node16 as base

WORKDIR /home/node
USER node

RUN git config --global url."https://".insteadOf git://
COPY --chown=node:node ./package.json package.json
COPY --chown=node:node ./package-lock.json package-lock.json
RUN npm install

COPY --chown=node:node ./ ./

EXPOSE 7100 7100

HEALTHCHECK --interval=1m --timeout=4s --start-period=30s \
  CMD curl -f http://localhost:7100/oauth2/.well-known/openid-configuration || exit 1

ENTRYPOINT ["/usr/local/bin/tini", "--"]
CMD ["node", "src/index.js"]
