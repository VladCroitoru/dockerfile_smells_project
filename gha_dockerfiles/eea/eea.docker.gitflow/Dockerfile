FROM python:3-alpine3.13
LABEL maintainer="EEA: IDM2 A-Team <eea-edw-a-team-alerts@googlegroups.com>"


RUN apk add --no-cache --virtual .run-deps git bash curl coreutils bc npm yarn jq  build-base gcc libffi-dev \
 && pip install docutils twine rstcheck \
 && pip install -I wheel==0.31.0 \
 && npm install -g release-it yarn-deduplicate

COPY src/* /

ENTRYPOINT ["/docker-entrypoint.sh"]
