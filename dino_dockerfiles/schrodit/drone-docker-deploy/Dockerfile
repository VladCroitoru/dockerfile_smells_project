FROM docker:17.12.1-ce-dind
RUN apk update && apk upgrade && \
    apk add --no-cache git openssh
ADD docker-deploy /bin/
ENTRYPOINT /bin/docker-deploy