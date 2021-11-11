FROM mhart/alpine-node:12 AS build
WORKDIR /app
COPY package.json package-lock.json tsconfig.json ./
COPY src ./src
RUN npm install \
  && npm run build-ts \
  && npm prune --production

RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 && \
  echo "37f2c1f0372a45554f1b89924fbb134fc24c3756efaedf11e07f599494e0eff9  /usr/local/bin/dumb-init" | sha256sum -c - && \
  chmod 755 /usr/local/bin/dumb-init

# Only copy over the node pieces we need from the above image
FROM mhart/alpine-node:slim-12 AS final
WORKDIR /app
COPY --from=build /usr/local/bin/dumb-init /usr/local/bin/dumb-init
COPY --from=build /app .
COPY . .
EXPOSE 28866
LABEL com.automatoninc.cog-for="Outreach"
ENTRYPOINT ["/usr/local/bin/dumb-init", "--", "node", "build/core/grpc-server.js"]
