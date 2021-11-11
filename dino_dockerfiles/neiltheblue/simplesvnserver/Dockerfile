
FROM alpine:3.4

RUN apk --no-cache add subversion

EXPOSE 3690

CMD svnserve -d --foreground -r /svn
