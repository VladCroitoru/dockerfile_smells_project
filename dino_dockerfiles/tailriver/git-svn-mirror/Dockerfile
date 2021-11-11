FROM alpine

ENV GIT_DIR=/work
RUN apk --no-cache add git-svn openssh perl-git subversion \
 && mkdir -p $GIT_DIR
ADD data/ /

ENTRYPOINT [ "/init.sh" ]
