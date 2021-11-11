FROM node:latest

MAINTAINER @huytbt

# Install software requirements
RUN apt-get update && \
apt-get install -y git

RUN npm install --global imagemin-cli

RUN npm install --global yarn

COPY ci-git-process /usr/bin/ci-git-process
RUN chmod 700 /usr/bin/ci-git-process

COPY ci-image-optimize /usr/bin/ci-image-optimize
RUN chmod 700 /usr/bin/ci-image-optimize

ENTRYPOINT ["ci-git-process", "ci-image-optimize"]
