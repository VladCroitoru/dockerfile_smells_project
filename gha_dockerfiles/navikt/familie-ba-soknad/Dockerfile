FROM navikt/node-express:16 as builder-base
USER root
RUN apk --no-cache add curl binutils make gcc g++ vips-dev
USER apprunner

COPY --chown=apprunner:apprunner ./yarn.lock ./package.json /var/server/


FROM builder-base as webpack-express-deps-builder
RUN yarn
# Trenger å vite BASE_PATH før vi kjører webpack, siden webpack bruker DefinePlugin for å videresende basepath til frontend
ARG base_path
ENV BASE_PATH=$base_path
ARG sentry_auth_token
ENV SENTRY_AUTH_TOKEN=$sentry_auth_token
ARG sentry_release
ENV SENTRY_RELEASE=$sentry_release

COPY --chown=apprunner:apprunner ./src /var/server/src
COPY --chown=apprunner:apprunner ./tsconfig* babel.config.cjs /var/server/


# Gjør faktisk bygg i eget steg slik at vi slipper å kjøre det i lokal stack
FROM webpack-express-deps-builder as webpack-express-builder
RUN yarn build


FROM builder-base as runtime-deps-builder
RUN yarn install --prod
RUN rm -rf .cache


FROM navikt/node-express:16 as prod-runner
USER root
RUN apk add vips-dev
USER apprunner

COPY --from=runtime-deps-builder /var/server/ /var/server
COPY --from=webpack-express-builder /var/server/build /var/server/build
COPY --from=webpack-express-builder /var/server/dist /var/server/dist

EXPOSE 9000
CMD ["yarn", "start"]
