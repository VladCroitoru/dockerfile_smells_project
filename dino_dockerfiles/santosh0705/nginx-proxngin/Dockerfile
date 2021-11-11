#
# nginx-proxngin Docker image building
#

#
#  From this base-image / starting-point
#
FROM alpine:3.3

#
#  Authorship
#
MAINTAINER Santosh Kumar Gupta <santosh0705@gmail.com>

#
#  Copy utilities and configuration files
#
ADD https://raw.githubusercontent.com/santosh0705/proxngin/master/proxngin /usr/sbin/proxngin
COPY s6 /etc/s6

#
#  Update packages
#  Install nginx, python
#  Clean up cache and unwanted things
#
RUN apk add --update nginx python s6 && \
    mkdir -p /etc/nginx/dynamic.d && \
    chmod +x /etc/s6/*/run /usr/sbin/proxngin && \
    ln -s /bin/true /etc/s6/nginx/finish && \
    ln -s /bin/true /etc/s6/proxngin/finish && \
    rm -rf /var/cache/apk/*

CMD ["/bin/s6-svscan", "/etc/s6"]
