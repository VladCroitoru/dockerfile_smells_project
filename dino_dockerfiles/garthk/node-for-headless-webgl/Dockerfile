FROM node:6
MAINTAINER Garth Kidd <garth@garthk.com>

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.description="Node with support for headless WebGL" \
      org.label-schema.name="node-for-headless-webgl" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.url="https://hub.docker.com/r/garthk/node-for-headless-webgl/" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/garthk/node-for-headless-webgl.git" \
      org.label-schema.version="1.0.0"

RUN apt-get update && apt-get install -y \
        libgl1-mesa-dri \
        libglapi-mesa \
        libosmesa6 \
        mesa-utils \
        xvfb \
 && apt-get clean

ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 /usr/bin/dumb-init
RUN chmod 0777 /usr/bin/dumb-init

ENTRYPOINT ["/usr/bin/dumb-init", "--", "xvfb-run", "-s", "-ac -screen 0 1280x1024x24"]
CMD ["node"]
