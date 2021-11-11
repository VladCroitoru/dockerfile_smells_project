FROM docker

RUN apk add --no-cache \
      curl \
      jq \
      py-pip \
      bash \
    && pip install awscli \
    && rm -rf /var/cache/apk/* \
    && curl -sL https://raw.githubusercontent.com/silinternational/ecs-deploy/develop/ecs-deploy > /usr/local/bin/ecs-deploy \
    && chmod a+x /usr/local/bin/ecs-deploy
