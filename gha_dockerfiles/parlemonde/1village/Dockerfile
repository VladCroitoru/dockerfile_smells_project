# STAGE 1 - Typescript to Javascript
FROM node:16.7-slim as build-dependencies

# Create app directory
WORKDIR /app

# Install app dependencies with yarn 2
COPY .yarn/releases .yarn/releases
COPY .yarn/sdks .yarn/sdks
COPY .yarn/cache .yarn/cache
COPY .yarnrc.yml .
COPY package.json .
COPY yarn.lock .
RUN yarn

# Bundle app source
COPY public public
COPY src src
COPY server server
COPY types types
COPY .env .
COPY .eslintignore .
COPY .eslintrc.js .
COPY .prettierrc.js .
COPY .svgrrc.js .
COPY nodemon.json .
COPY next-env.d.ts .
COPY next.config.js .
COPY tsconfig.json .
RUN mkdir dist

# Build sources
ENV NODE_ENV production
ENV DOCKER 1
RUN yarn build

# STAGE 2 - Docker server
FROM node:16.7-slim as prod

# Create app directory
WORKDIR /app

# Install app dependencies with yarn 2
COPY .yarn/releases .yarn/releases
COPY .yarn/sdks .yarn/sdks
COPY .yarn/cache .yarn/cache
COPY .yarnrc.yml .
COPY package.json .
COPY yarn.lock .
RUN yarn

# Copy app files
COPY next.config.js .
COPY --from=build-dependencies app/dist dist
COPY --from=build-dependencies app/public public

ENV DOCKER 1
ENV NODE_ENV production

EXPOSE 5000

CMD [ "yarn", "node", "./dist/server/app.js" ]
