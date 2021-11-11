ARG BUILD_IMAGE=node:14
ARG FILE_HOST_IMAGE=nginx:latest

#----------------------------------------------
#|  Build application in Node.js environment  |
#----------------------------------------------

# Build the application
FROM ${BUILD_IMAGE} AS builder

WORKDIR /application

# Retrieve all dependencies
COPY package.json ./
COPY yarn.lock ./

RUN yarn install --frozen-lockfile

# Build the application from source
COPY src/ ./src/
COPY public/ ./public/
COPY tsconfig.json ./
COPY config-overrides.js ./

RUN yarn build

#--------------------------------------------
#|  Production image to serve static files  |
#--------------------------------------------

FROM ${FILE_HOST_IMAGE} AS runner

# Allow the user to definte the path where the files will be hosted
ARG FILE_HOST_PATH=/usr/share/nginx/html

# Retrieve the application distributable from the builder
COPY --from=builder /application/build/ $FILE_HOST_PATH

ARG PORT=80

EXPOSE ${PORT}
