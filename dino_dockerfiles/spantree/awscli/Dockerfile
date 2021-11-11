FROM python:2.7-alpine

WORKDIR /tmp

ENV PAGER more

RUN \
  apk --no-cache add \
    bash \
    bash-completion \
    less \
    curl \
    jq

RUN \
  pip install --upgrade pip \
  && pip install --upgrade \
    awscli \
  && rm -rf /root/.cache

VOLUME ["~/.aws"]

ENTRYPOINT ["aws"]
