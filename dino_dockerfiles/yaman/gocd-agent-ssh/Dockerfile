FROM alpine:latest

LABEL gocd.version="17.7.0" \
  description="GoCD agent based on alpine version latest" \
  maintainer="GoCD <go-cd-dev@googlegroups.com>" \
  gocd.full.version="17.7.0-5147" \
  gocd.git.sha="53fdb1b15184f93966059a42429bf9ed0bfdee59"

ADD "https://download.gocd.org/binaries/17.7.0-5147/generic/go-agent-17.7.0-5147.zip" /tmp/go-agent.zip
ADD https://github.com/krallin/tini/releases/download/v0.14.0/tini-static-amd64 /usr/local/sbin/tini
ADD https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64 /usr/local/sbin/gosu

# allow mounting ssh keys, dotfiles, and the go server config and data
VOLUME /godata

# force encoding
ENV LANG=en_US.utf8

RUN \
  chmod 0755 /usr/local/sbin/tini && \
  chown root:root /usr/local/sbin/tini && \
  chmod 0755 /usr/local/sbin/gosu && \
  chown root:root /usr/local/sbin/gosu && \
  addgroup -g 1001 go && \ 
  adduser -D -u 1001 -G go go && \
  apk --update-cache upgrade && \ 
  apk add --update-cache openjdk8-jre-base git mercurial subversion openssh-client bash && \
  unzip /tmp/go-agent.zip -d / && \
  mv go-agent-17.7.0 /go-agent && \
  rm /tmp/go-agent.zip

ADD docker-entrypoint.sh /

RUN ["chmod", "+x", "/docker-entrypoint.sh"]

ENTRYPOINT ["/docker-entrypoint.sh"]
