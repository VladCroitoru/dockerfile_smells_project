# -- Base Node ---
FROM node:16-alpine AS base
WORKDIR /usr/src/app
COPY package*.json ./

# -- Build Base ---
FROM base AS build-base
COPY ["./jest.config.js", "./jest.setup.js", "./tsconfig.json", "./next-env.d.ts", "./.eslintrc", "./.eslintignore", "./"]

# -- Dependencies Node ---
FROM build-base AS dependencies
RUN npm set progress=false && npm config set depth 0
RUN npm install --only=production
RUN cp -R node_modules prod_node_modules
RUN npm install

# ---- Compile  ----
FROM build-base AS compile
COPY ./pages ./pages
COPY ./src ./src
COPY --from=dependencies /usr/src/app/node_modules ./node_modules
RUN npm run build

# ---- Release  ----
FROM base AS release
COPY --from=dependencies /usr/src/app/prod_node_modules ./node_modules
COPY --from=compile /usr/src/app/.next ./.next
COPY ./public ./public

# Expose port and define CMD
ENV NODE_ENV production
EXPOSE 80/tcp
CMD npm run start