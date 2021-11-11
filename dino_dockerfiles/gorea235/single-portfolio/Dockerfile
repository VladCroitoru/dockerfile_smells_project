FROM node:10.0.0-slim as base
WORKDIR /app
EXPOSE 80
ENV PORT=80

# ===== build container ======
FROM node:10.0.0 AS build
WORKDIR /src
COPY . .

# node locations
ENV NODE=node/
ENV NODE_M=node_modules/
ENV NODE_CONF=${NODE}tsconfig.node.json

# output locations
ENV DIST=dist/
ENV OUT=build/
ENV NG_OUT=${OUT}ng/
ENV NODE_OUT=${OUT}node/
ENV FULL_OUT=${OUT}out/
ENV FULL_OUT_NG=${FULL_OUT}content/

# do dependency restores here to allow caching
RUN yarn
RUN yarn --cwd ${NODE}
COPY ${NODE}${PKG} ${NODE_OUT}${PKG}
COPY ${NODE}${LOCK} ${NODE_OUT}${LOCK}
RUN yarn --prod --cwd ${NODE_OUT}

# do build
RUN make release-build

# ===== final container =====
FROM base AS final
COPY --from=build /src/build/out .
ENTRYPOINT ["node", "app.js"]
