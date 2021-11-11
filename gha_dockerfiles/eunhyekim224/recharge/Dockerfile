# Create build image
FROM node:14-alpine as build

# Set working directory
WORKDIR /app

# Add build binaries
# RUN apk add --no-cache --virtual .build-deps alpine-sdk python git

# Install development node modules
COPY package.json .
RUN yarn install --frozen-lockfile --pure-lockfile && yarn cache clean

# Set environment variables
ENV NODE_ENV production

# Copy build directory
COPY . .

# Run tests
FROM build as tests
RUN yarn test

# Install production dependencies

# Compile TS to JS
RUN yarn build

# Replace dev dependencies with prod dependencies
RUN yarn install --production --frozen-lockfile --pure-lockfile --prefer-offline --force && yarn cache clean

# Create final image
FROM node:14-alpine

# Set environment variables
ENV NODE_ENV production
ENV PORT 3000
ENV USER app

# Set work directory and
WORKDIR /${USER}

# Create non-root user
RUN addgroup -S ${USER} && adduser -S -G ${USER} ${USER}

# Copy from build
COPY --chown=${USER}:${USER} --from=build /${USER} /${USER}

# Set user
USER ${USER}

# Expose port
EXPOSE ${PORT}

# Run the web service on container startup.
CMD [ "yarn", "start" ]
