FROM node:8-alpine

RUN apk add --update git && \
    yarn global add conventional-github-releaser

WORKDIR "/project"

ENTRYPOINT ["/usr/local/bin/conventional-github-releaser"]
