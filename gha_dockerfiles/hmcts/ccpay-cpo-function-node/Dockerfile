FROM hmctspublic.azurecr.io/base/node:12-alpine as base

COPY --chown=hmcts:hmcts package.json yarn.lock ./
RUN yarn install --production  && rm -r ~/.cache/yarn

# ---- Runtime imge ----
FROM base as runtime
COPY . .