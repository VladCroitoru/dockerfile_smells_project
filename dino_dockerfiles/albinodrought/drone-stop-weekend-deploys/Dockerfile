FROM alpine:3.4
MAINTAINER AlbinoDrought <albinodrought@gmail.com>
LABEL maintainer="AlbinoDrought <albinodrought@gmail.com>"

LABEL org.label-schema.version=latest
LABEL org.label-schema.description="Drone plugin to fail the build if attempting to deploy on Friday, Saturday, or Sunday."
LABEL org.label-schema.url="https://github.com/AlbinoDrought/drone-stop-weekend-deploys"
LABEL org.label-schema.vcs-url="https://github.com/AlbinoDrought/drone-stop-weekend-deploys.git"
LABEL org.label-schema.name="Drone Stop Weekend Deploys"
LABEL org.label-schema.vendor="AlbinoDrought"
LABEL org.label-schema.schema-version="1.0"

RUN apk add --no-cache bash
COPY check.sh /usr/local/

ENTRYPOINT ["/usr/local/check.sh"]
