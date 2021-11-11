FROM ruby:2.3-alpine

ENV DOCKER_TEMPLATE_WRAPPER_HOME="/docker-template-wrapper" \
    PROJECT_HOME="/project" \
    PROJECT_URL=""

RUN mkdir $DOCKER_TEMPLATE_WRAPPER_HOME

COPY [ "./update-dockerfile", "./env.sh", "./Gemfile", "docker/entrypoint.sh", "${DOCKER_TEMPLATE_WRAPPER_HOME}/" ]

RUN    apk add --no-cache su-exec bash coreutils git alpine-sdk make \
    && bundler install --gemfile="${DOCKER_TEMPLATE_WRAPPER_HOME}/Gemfile" --system \
    && apk del --purge git alpine-sdk make \
    && rm -rf /var/cache/apk/*

VOLUME [ $PROJECT_HOME ]
WORKDIR $PROJECT_HOME
ENTRYPOINT [ "/docker-template-wrapper/entrypoint.sh" ]
CMD [ "--verbose" ]
