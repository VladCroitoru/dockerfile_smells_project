# ---- Base Node ----
FROM node:16-alpine AS base

# set working directory
WORKDIR /app


# ---- Dependencies ----
FROM base AS dependencies

RUN apk add --no-cache make gcc g++ python3

RUN npm set progress=false && npm config set depth 0

COPY package*.json ./
# only production dependencies so we can later use them in the final image
RUN npm install --only=production --loglevel info


# ---- Build ----
FROM dependencies AS build
# now also install dev dependencies required for the build
RUN npm install --loglevel info

#copy all project files
COPY . .
RUN npm run build


# ---- final ----
FROM base AS final
RUN apk add --no-cache curl

# --- Entrypoint ---
ENV HTTP_PORT=3000
EXPOSE 3000

HEALTHCHECK --interval=1m --timeout=20s --start-period=30s \
   CMD curl -f --max-time 18 "http://127.0.0.1:${HTTP_PORT}/health" || exit 1

CMD ["node","--enable-source-maps","/app/built/index.js","--patchall=run"]

VOLUME /app/log
VOLUME /app/db
#VOLUME /app/conf #need some work to move the config file into a seperate folder

# Copy files at last to maximise caching potential
COPY --from=dependencies /app/node_modules /app/node_modules
COPY --from=build /app/built /app/built
# For server-health endoint..
COPY --from=build /app/package.json /app/package.json