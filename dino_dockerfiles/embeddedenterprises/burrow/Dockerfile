FROM golang:alpine

LABEL vendor "EmbeddedEnterprises"
LABEL maintainers "Fin Christensen <fchristensen@embedded.enterprises>"

# Reasons for installs:
#  - curl: needed to install glide (later removed)
#  - git: needed to install dependencies from git
#  - openssh: needed to install git dependencies via ssh
RUN apk update && \
    apk add curl git openssh && \
    curl https://glide.sh/get | sh && \
    go get github.com/EmbeddedEnterprises/burrow && \
    apk del curl
