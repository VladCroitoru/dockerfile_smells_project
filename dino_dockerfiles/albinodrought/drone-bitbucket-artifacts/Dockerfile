FROM alpine:3.4
MAINTAINER AlbinoDrought <albinodrought@gmail.com>
LABEL maintainer="AlbinoDrought <albinodrought@gmail.com>"

LABEL org.label-schema.version=latest
LABEL org.label-schema.description="Drone plugin for deploying build artifacts to Bitbucket Downloads"
LABEL org.label-schema.url="https://github.com/AlbinoDrought/drone-bitbucket-artifacts"
LABEL org.label-schema.vcs-url="https://github.com/AlbinoDrought/drone-bitbucket-artifacts.git"
LABEL org.label-schema.name="Drone Bitbucket Artifacts"
LABEL org.label-schema.vendor="AlbinoDrought"
LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.docker.params="PLUGIN_AUTH_STRING=Bitbucket username and app-password pair,\
PLUGIN_REPO_OWNER=Owner of the Bitbucket repository,\
PLUGIN_REPO_SLUG=Slug of the Bitbucket repository,\
PLUGIN_FILE=File to be deployed to Bitbucket Downloads,\
DRONE_COMMIT_SHA=Hash of the triggering commit,\
PLUGIN_LINK=If set, link the deployed artifact,\
PLUGIN_ARTIFACT_KEY=Key to use for the linked artifact,\
PLUGIN_ARTIFACT_NAME=Name to use for the linked artifact,\
PLUGIN_ARTIFACT_DESCRIPTION=Description to use for the linked artifact"

RUN apk add --no-cache ca-certificates bash curl
COPY deploy.sh /usr/local/

ENTRYPOINT ["/usr/local/deploy.sh"]
