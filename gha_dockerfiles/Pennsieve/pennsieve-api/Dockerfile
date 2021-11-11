FROM pennsieve/sbt:1.2.3

ARG PENNSIEVE_NEXUS_USER
ARG PENNSIEVE_NEXUS_PW

COPY --chown=sbt:sbt project/build.properties project/plugins.sbt project/SecureDockerfile.scala ./project/
COPY --chown=sbt:sbt .sbtopts .
COPY --chown=sbt:sbt build.sbt .

RUN sbt update
