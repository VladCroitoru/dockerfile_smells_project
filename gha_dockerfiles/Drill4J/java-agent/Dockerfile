FROM ubuntu:20.04

ENV AGENT_VERSION $AGENT_VERSION

RUN apt-get update && apt-get install -y \
  wget \
  unzip \
  curl \
  jq \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /data-download/agent
RUN mkdir /data

COPY ./build/install/linuxX64/* /data-download/agent/
COPY commands.sh /commands.sh
COPY download-artifact.sh /download-artifact.sh

# Run the command on container startup
CMD ["/commands.sh"]
