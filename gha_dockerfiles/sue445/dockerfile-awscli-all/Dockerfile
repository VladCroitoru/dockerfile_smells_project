FROM alpine AS ecs-cli-downloader

RUN wget https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest -O /usr/local/bin/ecs-cli \
 && chmod 755 /usr/local/bin/ecs-cli

FROM python:3.7-alpine

ENV AWSCLI_VERSION 1.22.0

RUN apk --update --no-cache add bash git \
 && apk --update --no-cache add --virtual .build-deps gcc musl-dev \
 && pip install --no-cache-dir awscli==$AWSCLI_VERSION aws-sam-cli \
 && apk del .build-deps --purge

COPY --from=ecs-cli-downloader /usr/local/bin/ecs-cli /usr/local/bin/ecs-cli
