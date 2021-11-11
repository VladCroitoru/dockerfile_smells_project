# Build:
# docker build -t obigroup/svn .
#
# Run:
# docker run --rm -ti obigroup/svn version
# docker run --rm -v `pwd`:/src -ti obigroup/svn checkout URL[@REV]

FROM ubuntu:14.10
MAINTAINER Rony Dray <contact@obigroup.fr>
RUN apt-get update && apt-get install -y subversion

VOLUME ["/src"]
WORKDIR /src

ENTRYPOINT ["/usr/bin/svn"]
