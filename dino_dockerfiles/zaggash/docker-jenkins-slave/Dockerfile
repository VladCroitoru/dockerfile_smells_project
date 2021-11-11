FROM alpine

RUN \
  apk add --no-cache \
    --repository https://nl.alpinelinux.org/alpine/v3.6/community \
      ca-certificates \
      docker \
      openjdk8-jre \
      git \
      curl \
      wget && \

  LATEST=$(curl -sL https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/maven-metadata.xml | grep latest | tr "<" ">" | cut -d '>' -f 3) && \
  wget -q -O swarm-client.jar https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/${LATEST}/swarm-client-${LATEST}.jar
  
COPY entrypoint.sh /
RUN chmod +x entrypoint.sh
CMD ["/entrypoint.sh"]
