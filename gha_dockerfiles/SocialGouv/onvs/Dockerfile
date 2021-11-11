FROM node:15-alpine as builder

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install --frozen-lockfile --prefer-offline

COPY . ./

# May be not mandatory, since yarn install is supposed to run prisma generate initially
RUN yarn prisma generate

#
# NEXT_PUBLIC_ environment variables
#
# Next.js frontend variable are needed at build time
# because the frontend code is transpiled at build time
#
# as `yarn build` is executed INSIDE the Dockerfile
# then we need to use [docker ARG parameter](https://docs.docker.com/engine/reference/commandline/build/#set-build-time-variables---build-arg)
# to pass them to the docker build context
#
ARG NEXT_PUBLIC_MATOMO_URL
ARG NEXT_PUBLIC_MATOMO_SITE_ID
ARG NEXT_PUBLIC_ONVS_API_TOKEN
ARG NEXT_PUBLIC_SENTRY_DSN

ENV NEXT_PUBLIC_MATOMO_URL=$NEXT_PUBLIC_MATOMO_URL
ENV NEXT_PUBLIC_MATOMO_SITE_ID=$NEXT_PUBLIC_MATOMO_SITE_ID
ENV NEXT_PUBLIC_ONVS_API_TOKEN=$NEXT_PUBLIC_ONVS_API_TOKEN
ENV NEXT_PUBLIC_SENTRY_DSN=$NEXT_PUBLIC_SENTRY_DSN

ENV NEXT_TELEMETRY_DISABLED=1

RUN yarn build

# TODO: remove dev deps from final docker image
# RUN yarn install --production --frozen-lockfile --prefer-offline

USER node

ENV PORT=$PORT_ARG

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1

CMD ["yarn", "start"]
