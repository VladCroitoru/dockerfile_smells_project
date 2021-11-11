FROM ubuntu:20.04
LABEL mainatiner="Nico Kahlert nka@netzlink.com"

ENV RELEASE_VERSION=v0.15.2

COPY prerequisites.sh /prerequisites.sh
RUN /prerequisites.sh && rm /prerequisites.sh

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
