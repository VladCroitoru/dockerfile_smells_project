FROM ubuntu:14.04
MAINTAINER mookjp

VOLUME /data
EXPOSE 3690

RUN apt-get install subversion -y
RUN mkdir -p /var/svn/repo
RUN svnadmin create /var/svn/repo
CMD ["svnserve", "--foreground", "-d", "-r", "/var/svn/repo"]
