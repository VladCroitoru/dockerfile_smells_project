FROM alpine:latest

ARG VERSION
ARG BUILD_DATE
ARG VCS_REF
ARG GIT_COMMIT=unspecified

LABEL org.label-schema.version=$VERSION
LABEL org.label-schema.vcs-ref=$VCS_REF
LABEL org.label-schema.vcs-url=https://github.com/haenerconsulting/gitserver
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL git_commit=$GIT_COMMIT

EXPOSE 80

VOLUME ["/git", "/var"]

RUN apk add --no-cache \
  git-daemon \
  lighttpd \
  lighttpd-mod_auth 

COPY conf/* /etc/lighttpd/

CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]
