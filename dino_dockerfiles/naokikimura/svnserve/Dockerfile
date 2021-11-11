FROM alpine
MAINTAINER naokikimura <n.kimura.cap@gmail.com>

RUN apk update && apk add subversion

USER svn
RUN svnadmin create /var/svn/repos
VOLUME /var/svn/repos
EXPOSE 3690

ENTRYPOINT [ "/usr/bin/svnserve", "-d", "--foreground", "--root", "/var/svn/repos" ]
