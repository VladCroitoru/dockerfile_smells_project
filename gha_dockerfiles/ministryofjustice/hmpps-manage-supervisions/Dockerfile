# Stage: base image
FROM node:16-bullseye-slim as base
ARG BUILD_NUMBER
ARG GIT_REF

LABEL maintainer="HMPPS Digital Studio <info@digital.justice.gov.uk>"

ENV TZ=Europe/London
RUN ln -snf "/usr/share/zoneinfo/$TZ" /etc/localtime && echo "$TZ" > /etc/timezone

RUN addgroup --gid 2000 --system appgroup && \
    adduser --uid 2000 --system appuser --gid 2000

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN mkdir -p /usr/share/man/man1 /usr/share/man/man2
RUN apt-get install --no-install-recommends -y openjdk-11-jre-headless
RUN apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

# Stage: build app
FROM base as build
ARG BUILD_NUMBER
ARG GIT_REF

COPY . .

RUN CYPRESS_INSTALL_BINARY=0 npm ci --no-audit
RUN npm run build
RUN npm prune --no-audit --production

# Stage: copy production assets and dependencies
FROM base

COPY --from=build --chown=appuser:appgroup \
        /app/package.json \
        /app/package-lock.json \
        ./

COPY --from=build --chown=appuser:appgroup \
        /app/dist \
        ./dist

COPY --from=build --chown=appuser:appgroup \
        /app/node_modules \
        ./node_modules

EXPOSE 3000
ENV NODE_ENV='production'
USER 2000

CMD [ "npm", "start" ]
