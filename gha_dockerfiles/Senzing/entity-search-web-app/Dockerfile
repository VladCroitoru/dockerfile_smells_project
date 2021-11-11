ARG BUILD_IMAGE=node:14-buster-slim
ARG PROD_IMAGE=node:14-alpine
ARG TEST_IMAGE=node:14-buster-slim

FROM ${BUILD_IMAGE}
ENV REFRESHED_AT=2021-07-26

LABEL Name="senzing/entity-search-web-app" \
      Maintainer="support@senzing.com" \
      Version="2.3.3"

HEALTHCHECK CMD ["/app/healthcheck.sh"]

# Set working directory.
COPY ./rootfs /
WORKDIR /

# Add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# Install and cache app dependencies.
COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json
WORKDIR /app

RUN npm config set update-notifier false \
 && npm config set loglevel warn \
 && npm install \
 && npm install -g @angular/cli@10.0.0

# Build app
COPY . /app
RUN npm run build:docker

# production output stage
FROM ${PROD_IMAGE}
WORKDIR /app

# Copy files from repository.
COPY ./rootfs /
COPY ./run /app/run
COPY --from=0 /app/dist /app/dist
COPY --from=0 /app/package.json /app/package.json

RUN npm config set update-notifier false \
 && npm config set loglevel warn \
 && npm install --production

#COPY . /app
COPY --chown=1001:1001 ./proxy.conf.json /app

#USER 1001

# Runtime execution.

WORKDIR /app
ENTRYPOINT [ "npm", "run" ]
CMD ["start:docker"]
