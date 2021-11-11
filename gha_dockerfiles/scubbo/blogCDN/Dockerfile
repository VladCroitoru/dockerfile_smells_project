# Adapted from https://github.com/spurin/docker-hexo/blob/master/Dockerfile,
# with Github actions to build on Raspberry Pi-compatible architecture.
#
# Also removes the Github and ssh options since that's not needed for the
# self-hosting setup that is aimed for.

FROM node:13-slim

MAINTAINER Jack Jackson <scubbojj@gmail.com>

# Set the server port as an environment variable
ENV HEXO_SERVER_PORT=4000

# Without this line, we were getting `ESOCKETTIMEDOUT` when trying to `npm install`
# https://stackoverflow.com/a/37946399/1040915
ENV UV_THREADPOOL_SIZE=128

# Install requirements
RUN \
 apt-get update && \
 apt-get install git -y && \
 npm install -g hexo-cli

# Set workdir
WORKDIR /app

# Expose Server Port
EXPOSE ${HEXO_SERVER_PORT}

# Initialize hexo
# (Note that this diverges from the original image setup, since this
# assumes that there is no existing content - as doing `npm install`
# at runtime was causing timeouts)
# Note that this means this probably cannot be initialized with a
# mounted directory that contains existing content. I don't know
# whether it will overwrite existing content - beware!
#
# TODO - uncertain whether `npm install` _before_ `hexo` init will work.
RUN \
  npm install && \
  npm install --save hexo-admin

CMD \
  if [ "$(ls -A /app)" ]; then \
    echo "***** App directory exists and has content, continuing *****"; \
  else \
    echo "***** App directory is empty, initialising with hexo and hexo-admin *****" && \
    hexo init; \
  fi; \
  if [ ! -f /app/requirements.txt ]; then \
    echo "***** App directory contains no requirements.txt file, continuing *****"; \
  else \
    echo "***** App directory contains a requirements.txt file, installing npm requirements *****"; \
    cat /app/requirements.txt | xargs npm --prefer-offline install --save; \
  fi; \
  echo "***** Starting server on port ${HEXO_SERVER_PORT} *****" && \
  hexo server -d -p ${HEXO_SERVER_PORT}
