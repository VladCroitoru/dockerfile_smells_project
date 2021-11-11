FROM node:17.0.1-stretch-slim@sha256:73b366ccb9321c0298130163148535b82fed01e7712c66c6ae178009dfa1fb81 as base
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install --production
COPY . ./

FROM base as build
RUN yarn install
RUN yarn run format
RUN yarn run lint
RUN yarn run build

FROM node:17.0.1-stretch-slim@sha256:73b366ccb9321c0298130163148535b82fed01e7712c66c6ae178009dfa1fb81 as prod
WORKDIR /app
COPY --from=base /app/package.json ./
COPY --from=base /app/node_modules/ ./node_modules/
COPY --from=base /app/public/ ./public/
COPY --from=build /app/.next/ ./.next/
EXPOSE 3000
CMD ["yarn", "start"]