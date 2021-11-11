FROM jekyll/builder:latest

ARG REPOTOPUBLISH=Howtos
LABEL release_notes="this is a test release"
LABEL maintainer="camellzone@gmail.com"

EXPOSE 4000/tcp

RUN  mkdir /root/.ssh && yarn install

VOLUME ["/srv/jekyll", "/root/.ssh/"]
ENTRYPOINT echo "/srv/jekyll/$REPOTOPUBLISH" && cd /srv/jekyll/$REPOTOPUBLISH && pwd && git pull && cd /srv/jekyll/ && jekyll serve