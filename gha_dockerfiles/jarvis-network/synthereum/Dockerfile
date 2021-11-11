ARG NODE_VERSION=14.17.0

FROM node:${NODE_VERSION}-alpine as base
RUN apk add coreutils jq g++ git make python3 linux-headers eudev-dev libusb-dev
WORKDIR /src

# ------------------- Copy package.json and yarn.lock files ------------------ #
FROM base as yarn_lock
COPY . .
RUN mkdir /out \
  && JQ_EXPR='{ name, version, license, private, workspaces, resolutions, dependencies, devDependencies,' \
  && JQ_EXPR="${JQ_EXPR} scripts: .scripts | { preinstall, install, postinstall } | with_entries(select(.value != null)) }" \
  && git ls-files | grep "package.json" | tr '\n' '\0' | \
    xargs -0 -n1 sh -c 'x="/out/$1" && mkdir -p "${x%/*}" && cat "$1" | jq "'"$JQ_EXPR"'" > "$x"' -s \
  && cp yarn.lock /out

#RUN yarn set version berry
#RUN yarn plugin import typescript
#RUN yarn plugin import workspace-tools
#COPY .yarnrc.yml .yarnrc.yml

# --------------- Builder image with all dependencies installed -------------- #
FROM base as install
COPY --from=yarn_lock /out .
RUN yarn install --frozen-lock
RUN mkdir -p /out

# -------------- Project Builder image with everything installed ------------- #
FROM install as installed-project
COPY . .

# ---------------------------------------------------------------------------- #
#                                Build Frontend base                           #
# ---------------------------------------------------------------------------- #

FROM installed-project as build-frontend-base
# Keep in sync with docker-bake.hcl and apps/frontend/.env.example
ARG NEXT_PUBLIC_ONBOARD_API_KEY
ARG NEXT_PUBLIC_NETWORK_ID
ARG NEXT_PUBLIC_FORTMATIC_API_KEY_MAINNET
ARG NEXT_PUBLIC_FORTMATIC_API_KEY_TESTNET
ARG NEXT_PUBLIC_INFURA_API_KEY
ARG NEXT_PUBLIC_PORTIS_API_KEY
ARG NEXT_PUBLIC_PRICE_FEED_ROOT
ARG NEXT_PUBLIC_SUPPORTED_ASSETS

# ------------------------------ Build Frontend ------------------------------ #

FROM build-frontend-base as build-frontend
RUN yarn build frontend
RUN cp -r apps/frontend/out /out

# ------------------------------ Build Borrowing ------------------------------ #

FROM build-frontend-base as build-borrowing
RUN yarn build borrowing
RUN cp -r apps/borrowing/out /out

# -------------------------------- Build Claim -------------------------------- #

FROM build-frontend-base as build-claim
RUN yarn build claim
RUN cp -r apps/claim/out /out

# ---------------------------------------------------------------------------- #
#                       Frontend deployment final images:                      #
# ---------------------------------------------------------------------------- #

# ---------------------------- Netlify base image ---------------------------- #
FROM node:${NODE_VERSION}-alpine as netlify
RUN yarn global add netlify-cli

# ------------------ Exchange frontend Netlify deploy image: ----------------- #
FROM netlify as frontend
COPY --from=build-frontend /out /src

# ----------------- Borrowing frontend Netlify deploy image: ----------------- #
FROM netlify as borrowing
COPY --from=build-borrowing /out /src

# ------------------- Claim frontend Netlify deploy image: ------------------- #
FROM netlify as claim
COPY --from=build-claim /out /src

# ---------------------------------------------------------------------------- #
#                               Deploy Validator                               #
# ---------------------------------------------------------------------------- #

FROM base as prod_install
# Install only dependencies (no devDependencies)
RUN yarn install --production --frozen-lock
RUN mkdir -p /production_modules
RUN cp -r node_modules /production_modules

FROM node:${NODE_VERSION}-alpine as validator
WORKDIR /app
RUN  apk add --update --no-cache \
    ca-certificates \
    bash
COPY --from=prod_install /production_modules/* node_modules
COPY --from=build-libs /src/node_modules/@jarvis-network node_modules/@jarvis-network
COPY --from=build-validator  /out/ .
CMD ["node", "dist/index.js"]
