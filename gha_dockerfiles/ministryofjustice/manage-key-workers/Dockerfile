FROM node:14.17.4-buster
LABEL maintainer="HMPPS Digital Studio <info@digital.justice.gov.uk>"

ARG BUILD_NUMBER
ARG GIT_REF

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN addgroup --gid 2000 --system appgroup && \
    adduser --uid 2000 --system appuser --gid 2000

ENV TZ=Europe/London
RUN ln -snf "/usr/share/zoneinfo/$TZ" /etc/localtime && echo "$TZ" > /etc/timezone

# Create app directory
RUN mkdir /app && chown appuser:appgroup /app
USER 2000
WORKDIR /app
ADD --chown=appuser:appgroup . .

RUN CYPRESS_INSTALL_BINARY=0 npm ci --no-audit && \
    npm run build && \
    export BUILD_NUMBER=${BUILD_NUMBER} && \
    export GIT_REF=${GIT_REF} && \
    npm run record-build-info

ENV PORT=3000

EXPOSE 3000
USER 2000
CMD [ "npm", "start" ]
