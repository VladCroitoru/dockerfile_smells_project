# Install deps
FROM node:12 AS base
WORKDIR /base
COPY . .
RUN yarn install

# Building app
FROM base AS build
ENV NODE_ENV=production
WORKDIR /build
COPY --from=base /base ./
ENV NODE_ENV=production
RUN yarn run build

# Create production container
FROM node:12 AS production
ENV NODE_ENV=production
WORKDIR /app
COPY --from=build /build/package.json /build/yarn.lock ./
COPY --from=build /build/yarn.lock ./
COPY --from=build /build/.next ./.next
COPY --from=build /build/public ./public
RUN yarn install --frozen-lockfile --production && yarn cache clean

# Running the app
EXPOSE 3000
CMD [ "yarn", "start" ]
