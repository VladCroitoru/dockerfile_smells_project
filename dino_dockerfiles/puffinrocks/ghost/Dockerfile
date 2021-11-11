FROM ghost:latest

ENV VERSION=$GHOST_VERSION

COPY puffin-entrypoint.sh /
COPY config.js $GHOST_SOURCE/

ENTRYPOINT ["/puffin-entrypoint.sh"]
CMD ["node", "current/index.js"]
