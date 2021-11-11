FROM node:14-alpine3.13 as deps-dev

WORKDIR /deps

ARG REMIX_TOKEN

COPY package.json package-lock.json .npmrc ./

RUN npm ci --unsafe-perm

# ---

FROM node:14-alpine3.13 as deps-prod

WORKDIR /deps

ARG REMIX_TOKEN

COPY package.json package-lock.json .npmrc ./

ENV NODE_ENV=production

RUN npm ci --unsafe-perm

# ---

FROM node:14-alpine3.13 as build

ARG REMIX_TOKEN

ENV NODE_ENV=production

WORKDIR /build

COPY --from=deps-dev /deps/node_modules node_modules

COPY . .

RUN npm run build

# ---

FROM node:14-alpine3.13

WORKDIR /app

COPY package.json package-lock.json ./

COPY --from=deps-prod /deps/node_modules node_modules
COPY --from=build /build/build build
COPY --from=build /build/public public

ENV PATH="$PATH:node_modules/.bin"
ENV NODE_ENV="production"

ENTRYPOINT [ "npm" ]

CMD [ "run", "start" ]