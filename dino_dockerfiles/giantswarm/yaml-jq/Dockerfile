FROM python:3.6-alpine

RUN apk --no-cache add jq \
  && pip install pyyaml

COPY yaml-jq /usr/local/bin
ENTRYPOINT ["yaml-jq"]
