FROM efrecon/mini-tcl:3.7
MAINTAINER Emmanuel Frecon <efrecon@gmail.com>

# Ensure we have socat since nc on busybox does not support UNIX
# domain sockets.
RUN apk add --no-cache socat tini

# COPY code and documentation
COPY *.md /opt/withstander/
COPY *.tcl /opt/withstander/
COPY tockler/*.tcl /opt/withstander/tockler/

# Export where we will look for the Docker UNIX socket.
VOLUME ["/var/run/docker.sock"]

ENTRYPOINT [ "/sbin/tini", "--", "tclsh8.6", "/opt/withstander/withstander.tcl", "-docker", "unix:///var/run/docker.sock" ]
CMD ["-verbose", "INFO"]