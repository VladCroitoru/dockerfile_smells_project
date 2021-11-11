# This tag here should match the app's Meteor version, per .meteor/release
FROM geoffreybooth/meteor-base:2.3.6 AS meteor-builder

ARG APPNAME

# Make MATScommon discoverable
ENV METEOR_PACKAGE_DIRS=/MATScommon/meteor_packages

# Assume we're passed the repo root as build context
COPY apps/${APPNAME}/package*.json ${APP_SOURCE_FOLDER}/

RUN bash ${SCRIPTS_FOLDER}/build-app-npm-dependencies.sh

# Copy app & MATScommon library source into container
COPY apps/${APPNAME} ${APP_SOURCE_FOLDER}/
COPY MATScommon /MATScommon

RUN bash ${SCRIPTS_FOLDER}/build-meteor-bundle.sh


# Use the specific version of Node expected by your Meteor release, per https://docs.meteor.com/changelog.html
FROM node:14.17-alpine3.14

# Set Build ARGS
ARG APPNAME
ARG BUILDVER=dev
ARG COMMITBRANCH=development
ARG COMMITSHA

# Install runtime dependencies
RUN apk --no-cache add \
                    bash \
                    ca-certificates \
                    mariadb \
                    mongodb-tools \
                    python3 \
                    py3-numpy \
                    py3-pip \
    && pip3 --no-cache-dir install pymysql

# Set Environment
ENV APP_FOLDER=/usr/app
ENV APP_BUNDLE_FOLDER=${APP_FOLDER}/bundle
ENV SCRIPTS_FOLDER=/docker
ENV APPNAME=${APPNAME}
ENV SETTINGS_DIR=${APP_FOLDER}/settings/${APPNAME}
ENV MONGO_URL=mongodb://mongo:27017/${APPNAME}
ENV PORT=9000
ENV ROOT_URL=http://localhost:${PORT}/

# Copy in helper scripts
COPY --from=meteor-builder ${SCRIPTS_FOLDER} ${SCRIPTS_FOLDER}/

# Copy in app bundle
COPY --from=meteor-builder /opt/bundle ${APP_BUNDLE_FOLDER}/

# Copy in our launcher script
COPY container-scripts/run_app.sh ${APP_FOLDER}/

# Build Meteor dependencies, and create a writeable settings dir and Node fileCache
RUN bash ${SCRIPTS_FOLDER}/build-meteor-npm-dependencies.sh \
    && mkdir -p ${SETTINGS_DIR} \
    && chown -R node:node ${APP_FOLDER}/settings \
    && chmod -R 755 ${APP_FOLDER}/settings \
    && touch ${APP_BUNDLE_FOLDER}/bundle/programs/server/fileCache \
    && chown node:node ${APP_BUNDLE_FOLDER}/bundle/programs/server/fileCache \
    && chmod 644 ${APP_BUNDLE_FOLDER}/bundle/programs/server/fileCache

EXPOSE ${PORT}
USER node

WORKDIR ${APP_BUNDLE_FOLDER}/bundle

# Start app
# Note - meteor settings need to be mounted in as /usr/app/settings/${APPNAME} or else settings.json won't be picked up by run_app.sh
ENTRYPOINT ["/usr/app/run_app.sh"]

CMD ["node", "main.js"]

# Add Labels
LABEL version=${BUILDVER} code.branch=${COMMITBRANCH} code.commit=${COMMITSHA}
