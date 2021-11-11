FROM openjdk:alpine AS build
MAINTAINER Shane Mc Cormack <dataforce@dataforce.org.uk>

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV JAVA_TOOL_OPTIONS -Dfile.encoding=UTF8

COPY . /tmp/dfbnc/

RUN apk add --no-cache git coreutils bash

WORKDIR /tmp/dfbnc

# TODO: This bit is a little awful, and perhaps we should look at getting
#       rid of it at some point.
#
#       We want to unshallow the checkout and submodules to allow our build
#       process to have the full and complete git history for `git describe`
#       but that's really not the responsibility of the Dockerfile but actually
#       the CI system or whatever we're using.
#
#       To do this, we do a couple of things: Firstly, we fix the submodule
#       .git files to have a corrected path in them, and then we force the
#       .git/config to use http not ssh, and then we fetch and unshallow the
#       main repo and the submodules.
#
#       Leaving it in for now, but will look to remove in future.
#
#       I think this was mainly for DockerHub rather than Travis?
RUN \
  find -type f -name .git -exec bash -c 'f="{}"; cd $(dirname $f); echo "gitdir: ../../.git/modules/$(realpath --relative-to=/tmp/dfbnc .)" > .git' \; && \
  find .git -type f -name config -exec sed -i 's#url = git@github.com:#url = https://github.com/#g' {} \; && \
  if [ -e $(git rev-parse --git-dir)/shallow ]; then git init; git fetch --unshallow; fi && \
  git fetch --tags && \
  git submodule foreach 'if [ -e $(git rev-parse --git-dir)/shallow ]; then git init; git fetch --unshallow; fi' && \
  git submodule foreach 'git fetch --tags'

RUN ./gradlew jar


FROM openjdk:alpine AS run

RUN apk add --no-cache openssl

COPY --from=build /tmp/dfbnc/ssl.sh /home/dfbnc/ssl.sh
COPY --from=build /tmp/dfbnc/dist/dfbnc.jar /home/dfbnc/dfbnc.jar

RUN \
  addgroup -g 3456 -S dfbnc && \
  adduser -S -G dfbnc -u 3456 -s /bin/sh -h /home/dfbnc dfbnc && \
  mkdir /var/lib/dfbnc && \
  chown -R dfbnc /home/dfbnc && \
  chown -R dfbnc /var/lib/dfbnc && \
  chmod a+x /home/dfbnc/ssl.sh

USER dfbnc

EXPOSE 33262 33263

WORKDIR /var/lib/dfbnc

ENTRYPOINT ["/home/dfbnc/ssl.sh"]

CMD ["/usr/bin/java", "-jar", "/home/dfbnc/dfbnc.jar", "--config", "/var/lib/dfbnc", "--foreground"]
