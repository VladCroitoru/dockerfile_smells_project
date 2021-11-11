FROM mhart/alpine-node:14 as base

# Ensure application code makes it into the /app directory
COPY ./ /app/
WORKDIR /app

RUN export NODE_ENV=production && npm ci

####

FROM scratch
COPY --from=base / .

WORKDIR /app
ENTRYPOINT ["/usr/bin/node", "index.js"]



