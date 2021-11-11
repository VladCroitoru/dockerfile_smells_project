# Base image
FROM mhart/alpine-node:7

# Variables
ENV DOCKERIZE_VERSION v0.5.0
ENV DOCKERIZE_PATH https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}
ENV DOCKERIZE_ARCHIVE dockerize-alpine-linux-amd64-${DOCKERIZE_VERSION}.tar.gz

# Do everything
RUN apk add --no-cache curl \
  git \
  gzip \
  tar \
  && mkdir /app \
  && git clone https://github.com/DekodeInteraktiv/last-slack /app \
  && cd /app \
  && npm install \
  && rm -rf .git \
  && rm -rf /var/cache/apk/* \
  && rm -rf /root/.npm \
  && curl -LO ${DOCKERIZE_PATH}/${DOCKERIZE_ARCHIVE} \
  && tar xzf ${DOCKERIZE_ARCHIVE} \
  && rm -f ${DOCKERIZE_ARCHIVE} \
  && apk del curl \
  git \
  gzip \
  tar \
  && mv dockerize /usr/bin/dockerize \
  && chmod +x /usr/bin/dockerize

# Copy files into place
COPY files/* /app/

# Command to run
CMD /app/init.sh
