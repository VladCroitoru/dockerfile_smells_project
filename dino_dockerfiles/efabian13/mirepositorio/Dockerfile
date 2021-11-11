FROM library/debian:wheezy
MAINTAINER yo@e.es
RUN apt-get update && \
        apt-get install -y man funny-manpages
ENTRYPOINT ["/usr/bin/man"]
