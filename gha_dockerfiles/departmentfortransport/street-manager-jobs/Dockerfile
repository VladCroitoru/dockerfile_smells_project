ARG NODE_14_BASE_IMAGE

FROM $NODE_14_BASE_IMAGE AS base

RUN apk upgrade --no-cache && \
      mkdir -p /opt/app/dft-street-manager-jobs

WORKDIR /opt/app/dft-street-manager-jobs

ENTRYPOINT ["/sbin/tini", "--"]

COPY package.json .

COPY package-lock.json .

FROM base AS dependencies

RUN apk add --no-cache \
      git \
      g++ \
      make \
      openssh-client \
      python3

COPY . .

RUN mkdir ~/.ssh && \
  ssh-keyscan github.com > ~/.ssh/known_hosts && \
  cp .ssh/id_rsa ~/.ssh/id_rsa

RUN npm set progress=false && \
      npm config set depth 0 && \
      npm install --only=production && \
      cp -R node_modules prod_node_modules && \
      npm install && \
      npm run build && \
      npm run test && \
      npm run remove-dev-dependencies && \
      npx audit-ci --moderate

FROM base AS release

COPY --from=dependencies /opt/app/dft-street-manager-jobs/dist /opt/app/dft-street-manager-jobs/dist
COPY --from=dependencies /opt/app/dft-street-manager-jobs/src /opt/app/dft-street-manager-jobs/src
COPY --from=dependencies /opt/app/dft-street-manager-jobs/prod_node_modules /opt/app/dft-street-manager-jobs/node_modules

COPY --from=base /ca-certificates /ca-certificates

RUN chown nodejs:nodejs -R /opt/app /ca-certificates

USER nodejs
