FROM silintl/ecs-deploy:latest

RUN ln -s /ecs-deploy /usr/bin/

RUN apk update

RUN apk add docker

RUN mkdir -p /aws && \
    apk add groff less python py-pip && \
    pip install awscli && \
    apk --purge del py-pip && \
    rm /var/cache/apk/*

ENTRYPOINT []
