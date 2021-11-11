FROM node:current-bullseye-slim AS build

# Update Packages, Namely Python.
# Python is required for @tensorflow/tfjs-node
RUN apt-get update && \ 
    apt-get install -y build-essential \
    wget \
    python3 \
    make \
    gcc \ 
    libc6-dev 

WORKDIR /app
COPY . .

# Install, build and install packages for production
RUN npm ci
RUN npm run build
RUN npm ci --production --no-audit

FROM node:current-bullseye-slim AS deploy
WORKDIR /app
COPY --from=build /app .

ENV PORT=3000
EXPOSE $PORT
CMD [ "node", "./build" ]