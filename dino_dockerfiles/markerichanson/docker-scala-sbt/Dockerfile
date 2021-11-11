FROM markerichanson/docker-scala:2.11.8

ARG SBT_VERSION

RUN \
  curl -fsL https://piccolo.link/sbt-$SBT_VERSION.tgz | tar xfz - -C /usr/share/

ENV PATH /usr/share/sbt/bin:$PATH

WORKDIR /tmp


VOLUME ["/root/project"]
VOLUME ["/root/.ivy2"]

WORKDIR /root/project

#ENTRYPOINT ["sbt"]
