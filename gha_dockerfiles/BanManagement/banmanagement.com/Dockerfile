# ---- Base Node ----
FROM node:16-alpine AS base
## Install build toolchain, install node deps and compile native add-ons
RUN apk add --no-cache python3 make g++
# set working directory
WORKDIR /usr/src/app
# copy project file
COPY package*.json ./

#
# ---- Dependencies ----
FROM base AS dependencies
# install node packages
RUN npm set progress=false && npm config set depth 0
ENV NPM_CONFIG_LOGLEVEL warn
RUN npm ci --no-audit --only=production

#
# ---- Release ----
FROM base AS release
COPY --from=dependencies /usr/src/app/node_modules ./node_modules

# copy app sources
COPY . .

ENV NEXT_TELEMETRY_DISABLED 1
ENV NODE_ENV production

RUN npm run build

# expose port and define CMD
EXPOSE 3000

CMD npm start
