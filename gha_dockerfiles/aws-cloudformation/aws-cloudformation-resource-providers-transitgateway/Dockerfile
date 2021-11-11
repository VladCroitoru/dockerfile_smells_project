FROM python:alpine
MAINTAINER AWS
RUN apk add --update --no-cache \
      build-base \
      git \
      openssh-client \
      bash \
      curl

ARG GITHUB_ACTOR
ARG GITHUB_TOKEN
ARG APP_NAME
ENV GITHUB_ACTOR=$GITHUB_ACTOR

ENV APP_NAME=$APP_NAME

COPY . /app
WORKDIR /app
RUN git config --global user.email "${GITHUB_ACTOR}@users.no-reply.github.com"
RUN git config --global user.name "${GITHUB_ACTOR}"

RUN pip3 install pre-commit
CMD /bin/bash
