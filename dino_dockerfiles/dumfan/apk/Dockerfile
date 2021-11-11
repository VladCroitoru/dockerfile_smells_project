FROM geoffreybooth/meteor-base:1.10.1

COPY ./package*.json $APP_SOURCE_FOLDER/
RUN bash $SCRIPTS_FOLDER/build-app-npm-dependencies.sh

COPY . $APP_SOURCE_FOLDER/
RUN bash $SCRIPTS_FOLDER/build-meteor-bundle.sh

FROM node:12.16.1-alpine

ENV APP_BUNDLE_FOLDER /opt/bundle
ENV SCRIPTS_FOLDER /docker

RUN apk --no-cache add \
		bash \
		ca-certificates

COPY --from=0 $SCRIPTS_FOLDER $SCRIPTS_FOLDER/
COPY --from=0 $APP_BUNDLE_FOLDER/bundle $APP_BUNDLE_FOLDER/bundle/

RUN bash $SCRIPTS_FOLDER/build-meteor-npm-dependencies.sh

ENTRYPOINT ["/docker/entrypoint.sh"]

EXPOSE 3000

CMD ["node", "main.js"]
