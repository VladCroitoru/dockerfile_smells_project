# === Build stage ===

FROM node:12 as build

WORKDIR /build

# Install dependencies first, so the layer can be reused from cache when only the sources change
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

COPY . .
RUN yarn build

# === Production stage ===

FROM node:12-alpine

WORKDIR /app
COPY --from=build /build/build .
COPY --from=build /build/node_modules ./node_modules

EXPOSE 8080
ENV NODE_ENV=production
CMD [ "node", "index.js" ]
