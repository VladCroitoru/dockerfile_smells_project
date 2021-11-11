FROM hmctspublic.azurecr.io/base/node:12-alpine as base

ENV WORKDIR /opt/app
WORKDIR ${WORKDIR}

COPY --chown=hmcts:hmcts . .
RUN yarn install --production  && yarn cache clean

EXPOSE 3000
CMD [ "yarn", "start" ]
