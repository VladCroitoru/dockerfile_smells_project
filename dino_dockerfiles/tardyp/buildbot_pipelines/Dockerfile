# please follow docker best practices
# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/

FROM buildbot/buildbot-master:master

RUN \
    apk add --no-cache openssh && \
    pip install buildbot_pipelines && \
    rm -r /root/.cache

EXPOSE 8010
EXPOSE 9989
